from flask import Flask, render_template, request, jsonify, session
import json
import os
import sys
import uuid
from datetime import datetime

# Add the current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import from backend
try:
    from backend.Context import ContextManager
    from backend.Abstract import Abstraction
    from backend.Organizer import Organize
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure you have backend/__init__.py and all backend files")
    sys.exit(1)

# Initialize Flask app with explicit template and static folders
app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')
app.secret_key = 'your-secret-key-here-change-in-production'

# Initialize context manager
context_manager = ContextManager()

# ==================== JSON DATABASE FUNCTIONS ====================

def get_db_path():
    """Get the path to the database JSON file"""
    db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend', 'data')
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    return os.path.join(db_dir, 'scalpel_db.json')

def read_db():
    """Read the JSON database"""
    db_path = get_db_path()
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'prompts': [], 'code_generations': [], 'chats': [], 'sessions': []}

def write_db(data):
    """Write to the JSON database"""
    db_path = get_db_path()
    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, default=str)

def save_prompt(session_id, original, context_used, abstracted, organized):
    """Save a prompt to the database"""
    db = read_db()
    db['prompts'].append({
        'session_id': session_id,
        'original': original,
        'context_used': context_used,
        'abstracted': abstracted,
        'organized': organized,
        'timestamp': datetime.now().isoformat()
    })
    write_db(db)

def save_code_generation(session_id, prompt, code):
    """Save code generation to the database"""
    db = read_db()
    db['code_generations'].append({
        'session_id': session_id,
        'prompt': prompt,
        'code': code,
        'timestamp': datetime.now().isoformat()
    })
    write_db(db)

def save_chat(session_id, message, response, context_used):
    """Save chat to the database"""
    db = read_db()
    db['chats'].append({
        'session_id': session_id,
        'message': message,
        'response': response,
        'context_used': context_used,
        'timestamp': datetime.now().isoformat()
    })
    write_db(db)

def get_session_stats(session_id):
    """Get statistics for a session"""
    db = read_db()
    return {
        'prompts_optimized': len([p for p in db['prompts'] if p['session_id'] == session_id]),
        'code_generations': len([c for c in db['code_generations'] if c['session_id'] == session_id]),
        'chat_messages': len([c for c in db['chats'] if c['session_id'] == session_id])
    }

def get_chat_history(session_id, limit=50):
    """Get chat history for a session"""
    db = read_db()
    chats = [c for c in db['chats'] if c['session_id'] == session_id]
    chats.sort(key=lambda x: x['timestamp'], reverse=True)
    return chats[:limit]

# ==================== ROUTES ====================

@app.route('/')
def index():
    """Serve the main page"""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return render_template('index.html')

@app.route('/api/optimize', methods=['POST'])
def optimize_prompt():
    """Optimize the prompt using abstraction and organization"""
    try:
        data = request.json
        prompt = data.get('prompt', '')
        context = data.get('context', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Get context from chat history
        contextual_prompt = context_manager.get_context(prompt)
        
        # Apply abstraction to reduce size
        try:
            abstracted = Abstraction(contextual_prompt)
        except Exception as e:
            print(f"Abstraction error: {e}")
            abstracted = contextual_prompt[:1000]
        
        # Organize the prompt
        organized = Organize(abstracted)
        
        # Save to JSON database
        session_id = session.get('session_id', str(uuid.uuid4()))
        save_prompt(session_id, prompt, context, abstracted, organized)
        
        # Update context manager
        context_manager.add_message(prompt, 'user')
        context_manager.add_message(organized, 'assistant')
        
        return jsonify({
            'success': True,
            'optimized': organized,
            'abstracted': abstracted,
            'original_tokens': len(prompt) // 4,
            'optimized_tokens': len(organized) // 4,
            'message': 'Prompt optimized successfully'
        })
        
    except Exception as e:
        print(f"Optimization error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-code', methods=['POST'])
def generate_code():
    """Generate code based on the optimized prompt"""
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        # Generate code based on the prompt
        code = f"""# Generated Code from SCALPEL
# Based on prompt: {prompt[:200]}...

def solution():
    # TODO: Implement your solution here
    print("Code generated by SCALPEL")
    return True

if __name__ == "__main__":
    solution()
"""
        
        # Save to JSON database
        session_id = session.get('session_id', str(uuid.uuid4()))
        save_code_generation(session_id, prompt, code)
        
        return jsonify({
            'success': True,
            'code': code,
            'message': 'Code generated successfully'
        })
        
    except Exception as e:
        print(f"Code generation error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat interactions"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Add user message to context
        context_manager.add_message(message, 'user')
        
        # Get context for response
        context = context_manager.get_context(message)
        
        # Generate response
        response = f"I understand you're asking about: {message[:100]}... Could you be more specific about what you'd like to build?"
        
        # Add assistant response to context
        context_manager.add_message(response, 'assistant')
        
        # Save chat to JSON database
        session_id = session.get('session_id', str(uuid.uuid4()))
        save_chat(session_id, message, response, context)
        
        return jsonify({
            'success': True,
            'response': response,
            'exchange_count': len(context_manager.chat_history) // 2,
            'message': 'Chat processed successfully'
        })
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear-session', methods=['POST'])
def clear_session():
    """Clear the current session data"""
    try:
        # Clear context history
        context_manager.clear_history()
        
        # Clear session data
        session.clear()
        session['session_id'] = str(uuid.uuid4())
        
        return jsonify({
            'success': True,
            'message': 'Session cleared successfully'
        })
        
    except Exception as e:
        print(f"Clear session error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/session-stats', methods=['GET'])
def session_stats():
    """Get statistics for the current session"""
    try:
        session_id = session.get('session_id', str(uuid.uuid4()))
        stats = get_session_stats(session_id)
        
        return jsonify({
            'success': True,
            'stats': stats
        })
        
    except Exception as e:
        print(f"Session stats error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get chat history for the current session"""
    try:
        session_id = session.get('session_id', str(uuid.uuid4()))
        history = get_chat_history(session_id)
        
        return jsonify({
            'success': True,
            'history': history
        })
        
    except Exception as e:
        print(f"History error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/export-session', methods=['POST'])
def export_session():
    """Export all data for the current session"""
    try:
        session_id = session.get('session_id', str(uuid.uuid4()))
        db = read_db()
        
        session_data = {
            'session_id': session_id,
            'prompts': [p for p in db['prompts'] if p['session_id'] == session_id],
            'code_generations': [c for c in db['code_generations'] if c['session_id'] == session_id],
            'chats': [c for c in db['chats'] if c['session_id'] == session_id],
            'exported_at': datetime.now().isoformat()
        }
        
        # Save export to file
        export_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'exports')
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        
        export_file = os.path.join(export_dir, f'session_{session_id}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
        with open(export_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2)
        
        return jsonify({
            'success': True,
            'message': f'Session exported to {export_file}',
            'export_path': export_file
        })
        
    except Exception as e:
        print(f"Export error: {e}")
        return jsonify({'error': str(e)}), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Starting SCALPEL application...")
    print(f"📁 Project root: {os.path.dirname(os.path.abspath(__file__))}")
    print("🌐 Access at: http://localhost:5000")
    print("=" * 60)
    print("ℹ️  Press CTRL+C to stop the server")
    print("=" * 60)
    
    # Run with debug=True for development but use_reloader=False to prevent double loading
    app.run(
        debug=True, 
        host='0.0.0.0', 
        port=5000, 
        use_reloader=False
    )