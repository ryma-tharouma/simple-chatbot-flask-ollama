# Simple Local Chatbot 🔥

This is a **simple chatbot** app built with:

- **Flask** for the backend
- **HTML/JavaScript** for the frontend
- **Ollama** to run a local AI model (like Mistral)

The project runs completely **offline on your computer**.

---

## 🚀 Features

- Talk to Mistral (or any other Ollama model)
- Simple UI
- Easy to modify or extend

---

## 📦 Requirements

- Python 3.x
- Flask
- Requests
- Ollama installed locally

---

## 🛠 Installation

### 1. Install Ollama

Download and install from [https://ollama.com/download](https://ollama.com/download).

Test it:

```bash
ollama run mistral
```

---

### 2. Clone this repository

```bash
git clone https://github.com/ryma-tharouma/simple-chatbot-flask-ollama.git
cd simple-chatbot
```

---

### 3. Create and activate a virtual environment

```bash
python -m venv chatbot-env

# Activate it (Windows)
chatbot-env\Scripts\activate

# Or (Mac/Linux)
source chatbot-env/bin/activate
```

---

### 4. Install dependencies

```bash
pip install flask requests
```

---

## ⚙️ Usage

### 1. Start Ollama

```bash
ollama run mistral
```

Keep this terminal open.

---

### 2. Start the Flask app

```bash
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000/
```

---

### 3. Open your browser

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)  
Start chatting with your local AI model!

---

## 🐛 Troubleshooting

| Problem                  | Solution                                                |
| :----------------------- | :------------------------------------------------------ |
| Ollama command not found | Make sure Ollama is installed and running               |
| Flask errors             | Check if you installed `flask` and `requests` correctly |
| No response from AI      | Confirm Ollama server is active and model is loaded     |

---

## 📂 Project Structure

```bash
simple-chatbot/
│
├── app.py          # Flask backend
├── index.html      # Simple frontend
└── README.md       # Project instructions
```

---

## 📖 License

This project is open-source and free to use for learning purposes.
