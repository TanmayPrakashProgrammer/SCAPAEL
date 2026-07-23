# DEVELOEPER Guidelinces
___

As a Member of Enceladus Echo you have access to Use our Software and A right to changes in the app by Updating it

We welcome you to being a collaborator and a contributor of Scapel

Scapel is FREE to use by everyh member of **Enceladus Echo** and they have right to maintain the code and keep the changes 

Scapel can be use for your Personal Reasons and Hackathon Reasons but do not sell/upload to the Person who is outside of Encealadus Echo without any permission or Iniformation will loose your access as a Partner
____


### CODING ETHICS
___

 - For any Variables we will Use Snake - Case type Defining
  
   - MyName = 'Tanmay' is wrong
   - my_name = 'Tanmay' is right
   - age = 18 is wrong
   - info1_info2_age = 18 is write fo better context
 - do not use Raw Numebrs Use Variable Instead
 - Use a Better Structure for code and yes leave spaces if you want
 - Use Simple but Informative names as it can be possible for you
 - Never Push your code without testing it First test it check it and then push it 


___

### Meaning of Every FOLDER 

Yes you can see we have many folder here is You will lean the UseCase of EveryFolder

#### CONFIG
Not that Important but simple contains the constants things and configrations about your app to setup

Example::
```py
APP_NAME = "SCAPEL"
VERSION = "1.0.0"
THEME = "dark"
```

#### Flask Server Folder
This folder is the server side code of app which is reasponsible for the ouputs
Your App is just an Interface the main logic is written it here

It has an server.py which is the server file and we have teh utitlies like in the main Primary Folder casue it have some python files which have some specail type of funcitnos which will you write


#### Resources 

The Images, Icons and some acessorires will be stored in this folder

#### Themes 
It contains the qss fiels to run
which will decide you theme to the app

Example::
```css
QPushButton {
    border-radius:10px;
}
```
#### UI

it has teh UI Stuffs like 

 - Main Window
 - Login Window
 - FAQ
 - Settings
 - Buttons
 - Scroll Bars things

In a Python File Format


___

Every Time When You Bring a Update in a Project Scapel
You have to make a File named
Release_notes_Version 1_2_3_2 Type

Lets made this 
# 3. Flask Web Server

SCAPEL uses Flask as a communication layer between the Qt desktop application and external AI services.

The Flask server handles:

* API requests
* Data validation
* Communication with AI providers
* Response formatting
* Background server operations

## Flask Core Concepts

Developers should understand:

* Creating Flask applications
* Routes and URL mapping
* HTTP methods
* Request and response cycle
* JSON responses
* Request parsing

## Creating Flask Application

Basic structure:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "SCAPEL Server Running"


if __name__ == "__main__":
    app.run()
```

## HTTP Methods

SCAPEL APIs may use:

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Send new data |
| PUT    | Update data   |
| DELETE | Remove data   |

## Request Handling

Learn:

* request.get_json()
* request.args
* request.form
* URL parameters
* Request validation

Example:

```python
data = request.get_json()

prompt = data["prompt"]
```

## JSON Response Handling

Flask returns structured responses:

Example:

```json
{
    "status": "success",
    "response": "Improved prompt"
}
```

# Flask Server Configuration

Topics:

* Host configuration
* Port management
* Debug mode
* Secret keys
* Maximum request size
* Static files

# CORS Configuration

CORS allows communication between different applications.

SCAPEL requires understanding:

* What CORS is
* Flask-CORS extension
* Allowed origins
* Development vs production configuration

Example:

```python
from flask_cors import CORS

CORS(app)
```

# Flask Error Handling

Learn:

* HTTP status codes
* Custom error handlers
* Error response formatting
* Logging failures

Common errors:

| Code | Meaning      |
| ---- | ------------ |
| 400  | Bad Request  |
| 404  | Not Found    |
| 500  | Server Error |

# API Endpoint Design

Follow REST principles:

Example:

```
/api/v1/prompt/boost
/api/v1/history
/api/v1/settings
```

Good API design includes:

* Clear naming
* Version control
* Consistent responses
* Documentation

# Flask Running With Threads

Since SCAPEL is a desktop application, Flask runs in the background.

Architecture:

```
Qt Application

       |
       |

Background Thread

       |
       |

Flask Server
```

Important concepts:

* Background server startup
* Non-blocking execution
* Thread safety
* Multiple requests

# Environment Variables

Sensitive information should never be stored directly in code.

Example:

.env.example

```
GROK_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

Python loading:

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GROK_API_KEY")
```

Environment separation:

```
Development
      |
      |
.env


Production
      |
      |
Server Environment Variables
```

# Optional Flask Extensions

Useful extensions:

## Flask-SQLAlchemy

Database integration.

## Flask-Migrate

Database migration management.

## Flask-Login

Authentication system.

## Flask-SocketIO

Real-time communication.

---

# 4. HTTP and API Communication

SCAPEL communicates with external AI services using HTTP requests.

# Requests Library

Learn:

* GET requests
* POST requests
* PUT requests
* DELETE requests
* Headers
* JSON payloads
* Authentication
* File uploads

Example:

```python
import requests


response = requests.post(
    url,
    json=data,
    headers=headers
)
```

# Request Headers

Common headers:

```http
Authorization: Bearer API_KEY
Content-Type: application/json
```

# Response Handling

Learn:

* Status code checking
* JSON parsing
* Content handling
* Streaming responses
* Timeout management

Example:

```python
if response.status_code == 200:
    data = response.json()
```

# Session Management

Learn:

* requests.Session()
* Persistent connections
* Cookies
* Reusable headers

# API Error Handling

Handle:

* Connection failures
* Timeout errors
* Invalid responses
* Server errors
* Rate limits

# Retry System

Important concepts:

* Retry logic
* Exponential backoff
* Maximum retry limits

Example:

```
Request Failed

↓

Wait 2 seconds

↓

Retry

↓

Wait 4 seconds

↓

Retry Again
```

# URL Concepts

Understand:

* Base URLs
* Endpoints
* Query parameters
* Path parameters
* URL encoding

# API Testing

Tools:

* Postman
* Mock APIs
* API validation

---
# PyQt GUI Development Documentation

## 1. Introduction

SCAPEL uses PyQt to create the desktop graphical user interface.

PyQt provides Python bindings for the Qt framework, allowing developers to create modern desktop applications with:

* Windows
* Buttons
* Text fields
* Menus
* Dialogs
* Custom widgets
* Themes
* Event handling

The GUI layer is responsible only for user interaction.

The UI should not contain:

* AI processing logic
* API communication
* Database operations

Those tasks belong to the backend/core layer.

---

# 2. PyQt Application Structure

Recommended SCAPEL GUI structure:

```
ui/

├── MainWindow.py

├── SettingsWindow.py

├── AboutWindow.py

├── Widgets/
│   ├── PromptBox.py
│   ├── Sidebar.py
│   └── ResponseCard.py

└── Dialogs/
    ├── ApiKeyDialog.py
    └── ErrorDialog.py
```

---

# 3. QApplication

`QApplication` manages the entire desktop application.

Every PyQt application requires one QApplication instance.

Example:

```python
from PyQt6.QtWidgets import QApplication

app = QApplication([])

app.exec()
```

Responsibilities:

* Starts the event loop
* Handles application events
* Manages windows
* Controls application lifecycle

---

# 4. Main Window

SCAPEL's main interface is created using `QMainWindow`.

Example:

```python
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SCAPEL AI")
        self.resize(1200,800)
```

A main window can contain:

* Menu bar
* Tool bar
* Status bar
* Central widget

---

# 5. QWidget

`QWidget` is the base class for all GUI components.

Examples:

* Buttons
* Text boxes
* Custom components

Example:

```python
from PyQt6.QtWidgets import QWidget


class CustomWidget(QWidget):

    def __init__(self):
        super().__init__()
```

---

# 6. Layout Management

Layouts control how widgets are arranged.

## QVBoxLayout

Vertical arrangement.

Example:

```
Button

Button

Button
```

Code:

```python
layout = QVBoxLayout()

layout.addWidget(button)
```

---

## QHBoxLayout

Horizontal arrangement.

Example:

```
Button  Button  Button
```

---

## QGridLayout

Grid-based arrangement.

Example:

```
Name:     Input

Email:    Input
```

---

## QStackedLayout

Used for multiple pages.

Example:

```
Home Page

Settings Page

About Page
```

---

# 7. Important Widgets

## QLabel

Displays text or images.

Example:

```python
label = QLabel("SCAPEL AI")
```

---

## QPushButton

Creates clickable buttons.

Example:

```python
button = QPushButton("Boost Prompt")
```

---

## QLineEdit

Single-line input.

Example:

```python
username = QLineEdit()
```

---

## QTextEdit

Multi-line text input.

Used for:

* Prompt input
* AI responses

Example:

```python
prompt = QTextEdit()
```

---

## QListWidget

Displays lists.

Example:

Conversation history:

```
Chat 1
Chat 2
Chat 3
```

---

## QComboBox

Dropdown menu.

Example:

```
Select Model

Grok
GPT
Gemini
```

---

## QProgressBar

Shows progress.

Example:

```
Processing...

██████░░░░ 60%
```

---

# 8. Signals and Slots

PyQt uses signals and slots for event handling.

A signal means:

"Something happened."

A slot means:

"Function that runs after the event."

Example:

Button click:

```
User clicks button

        |

Signal

        |

Function executes
```

Code:

```python
button.clicked.connect(function_name)
```

Example:

```python
def boost_prompt():
    print("Boosting...")


button.clicked.connect(boost_prompt)
```

---

# 9. Custom Signals

For communication between threads or components.

Example:

```python
from PyQt6.QtCore import pyqtSignal


class Worker:

    finished = pyqtSignal()
```

---

# 10. Dialog Windows

Dialogs are popup windows.

Examples:

* Settings
* API Key input
* Error messages

## QMessageBox

Standard messages.

Example:

```python
QMessageBox.information(
    self,
    "Success",
    "Saved"
)
```

---

## Custom Dialog

Example:

```
ApiKeyDialog.py
```

Used for:

* API key entry
* User settings

---

# 11. Qt Stylesheets (QSS)

QSS is Qt's styling system.

It works similar to CSS.

Example:

```css
QPushButton {

    background-color: black;
    border-radius: 10px;

}
```

Used for:

* Dark themes
* Button designs
* Application appearance

---

# 12. Resources Management

GUI assets are stored separately.

Structure:

```
resources/

├── icons/

├── images/

├── fonts/

└── themes/
```

Examples:

Icons:

```
settings.png
home.png
send.png
```

Themes:

```
dark_theme.qss
light_theme.qss
```

---

# 13. Threading in PyQt

Long operations should not run on the main thread.

Bad:

```
Button Click

↓

AI Request

↓

GUI freezes
```

Correct:

```
Button Click

↓

Worker Thread

↓

AI Request

↓

Signal

↓

Update GUI
```

Important classes:

* QThread
* Worker objects
* pyqtSignal

---

# 14. SCAPEL GUI Workflow

Example:

```
User enters prompt

        |

PromptBox.py

        |

Signal

        |

Core PromptBooster.py

        |

AI API Request

        |

Response

        |

ResponseCard.py

        |

Display Result
```

---

# 15. GUI Development Rules

For SCAPEL:

1. UI files only handle interface.
2. Backend logic stays outside UI.
3. Reusable widgets should be separated.
4. Long tasks must use threads.
5. Avoid hardcoding paths.
6. Use resources folder for assets.
7. Keep windows modular.

---

# Recommended Learning Order

1. QApplication
2. QWidget
3. QMainWindow
4. Layouts
5. Widgets
6. Signals and Slots
7. Dialogs
8. QSS Styling
9. Threads
10. Model-View Architecture

---

This documentation defines the standard for creating and maintaining SCAPEL's Qt interface.


# HTTP and HTTPS Communication in Python Documentation

## 1. Introduction

HTTP (HyperText Transfer Protocol) is a communication protocol used for transferring data between applications over a network.

In SCAPEL, HTTP is used for communication between:

```text
Qt Desktop Application

        |

        HTTP Request

        |

Flask Local Server

        |

        HTTP Request

        |

AI API Provider
```

HTTPS is the secure version of HTTP that encrypts communication using TLS encryption.

---

# 2. HTTP vs HTTPS

## HTTP

HTTP transfers data without encryption.

Example:

```text
Client  ------------->  Server

        Request

Client  <-------------  Server

        Response
```

Problems:

* Data can be intercepted
* Not suitable for sensitive information
* API keys should never be sent through plain HTTP over the internet

---

## HTTPS

HTTPS adds encryption.

Example:

```text
Client

   |
   |
Encrypted Connection

   |
   |

Server
```

Benefits:

* Data encryption
* Identity verification
* Protection against interception

---

# 3. HTTP Request Structure

A request contains:

## Method

Defines the action.

Common methods:

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Send data     |
| PUT    | Update data   |
| DELETE | Remove data   |

Example:

```http
POST /api/prompt
```

---

## Headers

Headers contain additional information.

Example:

```http
Content-Type: application/json
Authorization: Bearer API_KEY
```

Common headers:

* Content-Type
* Authorization
* User-Agent
* Accept

---

## Body

Contains the actual data.

Example:

```json
{
    "prompt": "Improve this code"
}
```

---

# 4. Python HTTP Requests

Python commonly uses the `requests` library.

Installation:

```bash
pip install requests
```

---

# 5. GET Request

Example:

```python
import requests


response = requests.get(
    "https://api.example.com/data"
)

print(response.text)
```

Used for:

* Fetching data
* Getting information

---

# 6. POST Request

Used to send data.

Example:

```python
import requests


data = {
    "prompt": "Optimize Python code"
}


response = requests.post(
    "https://api.example.com/boost",
    json=data
)
```

---

# 7. Sending Headers

Example:

```python
headers = {

    "Authorization": "Bearer API_KEY",

    "Content-Type": "application/json"

}


response = requests.post(
    url,
    headers=headers,
    json=data
)
```

---

# 8. JSON Handling

Convert response into Python objects:

```python
response_data = response.json()
```

Example response:

```json
{
    "status": "success",
    "answer": "Improved code"
}
```

Python:

```python
print(response_data["answer"])
```

---

# 9. HTTP Status Codes

Servers return status codes.

Common codes:

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

Example:

```python
if response.status_code == 200:

    print("Success")

else:

    print("Failed")
```

---

# 10. Error Handling

Network requests can fail.

Common problems:

* No internet connection
* Server unavailable
* Timeout
* Invalid API key
* Rate limit exceeded

Example:

```python
import requests


try:

    response = requests.get(
        url,
        timeout=5
    )

except requests.exceptions.Timeout:

    print("Server took too long")

except requests.exceptions.ConnectionError:

    print("Connection failed")
```

---

# 11. Timeout Management

Never allow unlimited waiting.

Bad:

```python
requests.get(url)
```

Good:

```python
requests.get(
    url,
    timeout=10
)
```

---

# 12. API Authentication

APIs usually require authentication.

Common methods:

## API Key

Example:

```http
Authorization: Bearer API_KEY
```

## Token Authentication

Example:

```http
Authorization: Bearer TOKEN
```

---

# 13. HTTPS Certificates

HTTPS verifies the server identity using certificates.

Python automatically verifies certificates.

Example:

```python
requests.get(
    "https://example.com"
)
```

Certificate verification:

```python
requests.get(
    url,
    verify=True
)
```

---

# 14. Localhost Communication

SCAPEL uses local communication.

Example:

```text
Qt Application

        |

http://127.0.0.1:5000

        |

Flask Server
```

Example request:

```python
requests.post(
    "http://127.0.0.1:5000/boost",
    json=data
)
```

---

# 15. Flask HTTP Server Example

Server:

```python
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/boost", methods=["POST"])
def boost():

    data = request.json

    return jsonify({

        "result": "Prompt improved"

    })


app.run(port=5000)
```

---

# 16. SCAPEL Communication Flow

Complete flow:

```text
User

 |

Qt PromptBox

 |

HTTP POST Request

 |

Flask Server

 |

Prompt Processing

 |

AI API HTTPS Request

 |

AI Response

 |

Flask Response

 |

Qt Interface Update
```

---

# 17. Security Guidelines

For SCAPEL:

1. Always use HTTPS for external APIs.
2. Never send API keys from the client.
3. Store secrets using environment variables.
4. Validate all incoming requests.
5. Use timeouts.
6. Handle API failures gracefully.
7. Do not trust user input directly.

---

# 18. Libraries Used in Python

Common HTTP libraries:

| Library  | Usage                   |
| -------- | ----------------------- |
| requests | Simple HTTP requests    |
| httpx    | Modern async HTTP       |
| urllib   | Built-in Python library |
| aiohttp  | Async networking        |

---

# Recommended Learning Order

1. HTTP basics
2. Request methods
3. Headers
4. JSON communication
5. Requests library
6. Flask APIs
7. Authentication
8. HTTPS security
9. Async communication

---

This documentation covers the HTTP/HTTPS knowledge required for SCAPEL's Qt application, Flask server, and AI API communication.
