import os
import requests
from bs4 import BeautifulSoup
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.schema import Document

# Set Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("google_api_key", "")

# Sample URLs to load content
urls = [
    "https://www.thapar.edu/",
    "https://www.thapar.edu/admissions/pages/admissions",
]

def fetch_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup(['script', 'style']):
        tag.decompose()
    return soup.get_text(separator='\n', strip=True)

web_texts = [fetch_text_from_url(url) for url in urls]
web_docs = [Document(page_content=text, metadata={"source": urls[i]}) for i, text in enumerate(web_texts)]

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(web_docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(chunks, embeddings)

llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-pro")

qa_system = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever()
)

def get_answer(query):
    result = qa_system.invoke(query)
    return result["result"]