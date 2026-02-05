# 🧠 Log Reader — AI-Powered Log to JSON Converter

This project uses **Google Gemini API** to automatically read, clean, and convert a log file into a structured **JSON** format.

---

## 🚀 Features
- Reads raw log files from the `assets/` directory  
- Removes empty lines and joins them into a single text block  
- Sends the log content to **Gemini AI** for structured analysis  
- Generates **PEP8-compliant JSON** output  
- Saves the result into a `.json` file  

---

## 📦 Requirements
Make sure you have:
- Python **3.10+**
- A **Google Gemini API key**
- Installed dependencies:
  ```bash
  pip install google-genai python-dotenv
  ```

---

## ⚙️ Environment Setup
Create a `.env` file in the project root with your API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

Example structure:
```
project/
│
├── assets/
│   └── log.log
│
├── logreader.py
├── .env
├── .gitignore
└── requirements.txt
```

---

## 🧩 Usage
Run the script from your terminal:

```bash
python logreader.py log.log output
```

- **First argument:** path to your log file (inside `assets/`)
- **Second argument (optional):** output file name (default = `output.json`)

Example:
```bash
python logreader.py server.log output
```
