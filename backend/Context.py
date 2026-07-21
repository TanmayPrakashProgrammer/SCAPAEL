import re
import sys
import os

# Add the parent directory to path so we can import Abstract
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from backend.Abstract import Abstraction
except ImportError:
    # Fallback to relative import
    from .Abstract import Abstraction

class ContextManager:
    def __init__(self):
        self.chat_history = []
        self.session_id = None
        self.max_context_messages = 5  # Keep last 5 messages for context
    
    def add_message(self, message, role='user'):
        """Add a message to chat history"""
        self.chat_history.append({
            'role': role,
            'content': message,
            'timestamp': None
        })
        # Keep only last 10 messages to prevent memory issues
        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]
    
    def get_context(self, current_prompt, max_tokens=1000):
        """
        Get relevant context from chat history for the current prompt.
        Returns combined context string.
        """
        if not self.chat_history:
            return current_prompt
        
        # Get last N user messages for context
        user_messages = [msg['content'] for msg in self.chat_history 
                        if msg['role'] == 'user']
        
        # If no user messages, return just the current prompt
        if not user_messages:
            return current_prompt
        
        # Combine all user messages with the current prompt
        combined = " ".join(user_messages[-self.max_context_messages:])
        combined += " " + current_prompt
        
        # Apply abstraction to reduce size while keeping meaning
        try:
            abstracted = Abstraction(combined)
            # If abstraction made it too small or empty, keep combined
            if len(abstracted) < 10:
                return combined
            return abstracted
        except Exception as e:
            print(f"Abstraction error: {e}")
            # If abstraction fails, return combined with token limit
            if len(combined) > max_tokens * 4:
                return combined[:max_tokens * 4]
            return combined
    
    def clear_history(self):
        """Clear chat history"""
        self.chat_history = []
    
    def get_history_summary(self):
        """Get a summary of the chat history"""
        return {
            'total_messages': len(self.chat_history),
            'user_messages': [msg['content'] for msg in self.chat_history 
                            if msg['role'] == 'user'],
            'assistant_messages': [msg['content'] for msg in self.chat_history 
                                 if msg['role'] == 'assistant']
        }