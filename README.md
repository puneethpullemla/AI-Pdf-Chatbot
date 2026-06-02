# 🚀 AI PDF Chatbot – RAG-Based Question Answering System

An intelligent AI-powered chatbot that allows users to upload PDF documents and ask questions in natural language. The system uses **Retrieval-Augmented Generation (RAG)**, **LangChain**, **FAISS**, **Sentence Transformers**, and **FLAN-T5** to retrieve relevant document content and generate accurate context-aware answers.

## 🌐 Live Demo

https://ai-pdf-chatbot-nxgzdrmssrncf7mszyeus4.streamlit.app/


---

## 🌟 Features

✅ Upload and analyze PDF documents

✅ Semantic search using vector embeddings

✅ Retrieval-Augmented Generation (RAG)

✅ Context-aware question answering

✅ FAISS-powered vector database

✅ Hugging Face Transformer integration

✅ Streamlit interactive web interface

✅ Fast document retrieval and response generation

---

## 🏗️ System Architecture

```text
PDF Document
      │
      ▼
PDF Loader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformers
(all-MiniLM-L6-v2)
      │
      ▼
Vector Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Relevant Context Retrieval
      │
      ▼
FLAN-T5 LLM
      │
      ▼
Generated Answer
```

---

## 🧠 Tech Stack

### AI & NLP

- LangChain
- Hugging Face Transformers
- FLAN-T5
- Sentence Transformers
- Semantic Search
- Retrieval-Augmented Generation (RAG)

### Vector Database

- FAISS

### Backend

- Python

### Frontend

- Streamlit

### PDF Processing

- PyPDF
- PDFPlumber

---

## 📂 Project Structure

```text
AI-PDF-Chatbot/
│
├── data/
│   └── sample.pdf
│
├── utils/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── llm.py
│
├── streamlit_app.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

### Step 1: PDF Upload

The user uploads a PDF document.

### Step 2: Document Processing

The PDF is converted into text and split into smaller chunks.

### Step 3: Embedding Generation

Each chunk is transformed into vector embeddings using:

```python
all-MiniLM-L6-v2
```

### Step 4: Vector Storage

Embeddings are stored in a FAISS vector database.

### Step 5: Question Retrieval

When a user asks a question:

- Similar chunks are retrieved from FAISS
- Relevant context is selected

### Step 6: Answer Generation

The retrieved context is sent to FLAN-T5 which generates the final answer.

---

## 📈 Key Achievements

- Built a complete Retrieval-Augmented Generation (RAG) pipeline.
- Implemented semantic search using Sentence Transformers and FAISS.
- Processed and indexed PDF documents for intelligent retrieval.
- Integrated Hugging Face FLAN-T5 for context-aware answer generation.
- Developed an end-to-end AI application using LangChain.
- Improved answer relevance through vector similarity search.

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/puneethpullemla/AI-Pdf-Chatbot.git

cd AI-Pdf-Chatbot
```

### Create Virtual Environment

```bash
python -m venv chatbot

chatbot\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

### Streamlit Version

```bash
streamlit run streamlit_app.py
```

### Command Line Version

```bash
python app.py
```

---

## 🔍 Example Questions

```text
What is Artificial Intelligence?

Explain Machine Learning.

Summarize this document.

What technologies are mentioned in the PDF?

What is Retrieval-Augmented Generation?
```

---

## 📸 Sample Output

```text
Question:
What is Artificial Intelligence?

Answer:
Artificial Intelligence (AI) is a field of computer science focused on creating systems capable of performing tasks that normally require human intelligence such as learning, reasoning, decision-making, and language understanding.
```

---

## 🎯 Skills Demonstrated

- Machine Learning
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Embeddings
- Vector Databases (FAISS)
- LangChain
- Hugging Face Transformers
- Prompt Engineering
- Information Retrieval
- Model Deployment
- Python Development

---

## 🚀 Future Enhancements

- Multi-PDF Support
- Chat History Memory
- Source Citations
- Hybrid Search (BM25 + Vector Search)
- FastAPI Backend
- Docker Deployment
- Cloud Deployment (AWS/GCP/Azure)
- Support for Advanced Open-Source LLMs (Llama, Mistral, Gemma)

---

## 👨‍💻 Author

**Puneeth Kumar**

📧 puneethpullemla@gmail.com

🔗 GitHub: https://github.com/puneethpullemla

🔗 LinkedIn: https://www.linkedin.com/in/puneethpullemla/

---

## ⭐ Star This Repository

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.
