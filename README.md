# 🤖 AI-Powered Chatbot Using Llama 3

## Overview

This project is an AI-powered chatbot built using Python, Streamlit, and Ollama (Llama 3). The chatbot provides real-time conversational responses through an interactive web interface.

The application demonstrates the integration of a Large Language Model (LLM) with a user-friendly frontend, enabling users to ask questions and receive AI-generated responses locally.

---

## Features

* 💬 Interactive chat interface
* 🤖 AI-generated responses using Llama 3
* 📝 Chat history management
* 🗑️ Clear chat functionality
* ⚡ Real-time response generation
* 🎨 User-friendly Streamlit interface
* 🔒 Local execution using Ollama

---

## Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3
* Requests Library

---

## Project Structure

AI-Powered-Chatbot/

├── app.py

├── requirements.txt

├── README.md

├── screenshots/

│   ├── home.png

│   └── chat.png

└── .gitignore

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/adhithyanms25/AI-Powered-Chatbot-Using-Llama3.git
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux/Mac:

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Run the model:

```bash
ollama run llama3
```

---

## Run the Application

```bash
streamlit run app.py
```

Open the URL displayed in the terminal, typically:

```text
http://localhost:8501
```

---

## How It Works

1. User enters a question in the chat interface.
2. The application sends the prompt to the Ollama API.
3. Llama 3 processes the prompt.
4. The generated response is returned to the Streamlit application.
5. The response is displayed and stored in chat history.

---

## Screenshots

### Home Screen

<img width="960" height="436" alt="chatbot_ui" src="https://github.com/user-attachments/assets/52936fef-1f11-40e1-bced-f23850294a33" />


### Chat Interface

<img width="1920" height="1008" alt="chatbot_demo" src="https://github.com/user-attachments/assets/4204f64e-9f68-42f3-9e03-e9b48369fc2c" />


---

## Future Enhancements

* Voice input support
* Text-to-speech responses
* PDF document question answering
* Multi-model selection
* Chat export functionality
* Conversation memory
* Cloud deployment

---

## Author

Adhithyan M S

---

## License

This project is developed for learning and educational purposes.
