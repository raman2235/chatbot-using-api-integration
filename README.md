# 🤖 Gemini RAG Chatbot (LangChain + Streamlit)

This is a chatbot app that uses Google's Gemini model via LangChain and Chroma vector store. It retrieves answers based on scraped content (like university websites).

## 🚀 Features
- Gemini 1.5 integration
- LangChain document loader + vector store
- RAG (Retrieval-Augmented Generation)
- Streamlit web UI

## 💡 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🔐 Secrets for Streamlit Cloud
Go to `.streamlit/secrets.toml` and add:

```toml
google_api_key = "YOUR_GEMINI_API_KEY"
```

## 🌍 Deployment
Deploy on [streamlit.io/cloud](https://streamlit.io/cloud)

---