# Gemini-powered QA Chatbot

This project is a **Retrieval-based Question Answering Chatbot** using **Google Gemini API** and **LangChain**.  
It integrates data from **Thapar University webpages** and uploaded documents (PDF, DOCX, TXT).

---

## Features
- Fetches and cleans text from websites
- Supports PDF, DOCX, TXT uploads
- Uses Sentence Transformers for embeddings
- Stores vectors in ChromaDB
- Powered by Gemini 1.5 Pro
- Exposes REST API with Flask

---

## Installation
```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
pip install -r requirements.txt
```

---

## Environment Variable
Set your Gemini API key:
```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

---

## Run Locally
```bash
python app.py
```
API will run at `http://127.0.0.1:5000/`

Example:
```bash
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"Tell me about Thapar scholarships"}'
```

---

## Deployment
- **Render**: set build `pip install -r requirements.txt`, start `gunicorn app:app`
- **Heroku**: use Procfile, add `GOOGLE_API_KEY`

---
