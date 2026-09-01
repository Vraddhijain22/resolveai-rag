# ResolveAI — Enterprise Knowledge Assistant

🚀 **Live Demo:** https://resolveai-rag-project.streamlit.app/

ResolveAI is an AI-powered enterprise knowledge assistant built using
**Retrieval-Augmented Generation (RAG)**.

The system helps employees find answers from internal company policies,
SOPs, and troubleshooting documentation through a simple conversational
interface.

---

## 🎯 Problem

Employees often need to search through multiple internal documents to find
answers about:

- IT troubleshooting
- Password management
- Travel reimbursement
- Expense approval
- Security procedures
- Company policies

ResolveAI provides a conversational interface that retrieves relevant
information from company documents and generates grounded answers using an
LLM.

---

## 🚀 Features

- PDF document ingestion
- Multi-document processing
- PDF text extraction using PyPDF
- Text chunking with overlap
- Metadata tracking for document and page
- Gemini-powered text embeddings
- Semantic similarity search
- Qdrant Cloud vector database
- Top-K document retrieval
- Relevance checking
- Gemini-powered answer generation
- Source document attribution
- Page-level source information
- Relevance scores
- LangGraph-based RAG workflow
- Interactive Streamlit interface
- Cloud deployment

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **Google Gemini**
  - Gemini Embeddings
  - Gemini LLM
- **Qdrant Cloud**
- **PyPDF**
- **Streamlit**
- **Git**
- **GitHub**

---

## 🧠 RAG Pipeline

```text
PDF Documents
      ↓
Document Ingestion
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Gemini Embeddings
      ↓
Qdrant Cloud
      ↓
User Question
      ↓
Question Embedding
      ↓
Semantic Similarity Search
      ↓
Relevant Document Chunks
      ↓
Relevance Check
      ↓
Gemini LLM
      ↓
Grounded Answer
      ↓
Source + Page + Relevance Score
```

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   PDF Documents     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Document Processing │
                    │    + Chunking       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Gemini Embeddings   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Qdrant Cloud     │
                    │   Vector Database   │
                    └──────────┬──────────┘
                               │
                         Retrieval
                               │
                               ▼
┌─────────────────┐   ┌─────────────────────┐
│  User Question  │──▶│  LangGraph RAG      │
└─────────────────┘   │     Workflow        │
                      └──────────┬──────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │  Relevance Check    │
                      └──────────┬──────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │     Gemini LLM      │
                      └──────────┬──────────┘
                                 │
                                 ▼
                      ┌─────────────────────┐
                      │ Answer + Sources    │
                      └─────────────────────┘

```

---

## ☁️ Deployment

The application is deployed using **Streamlit Cloud**.

---

## 🔮 Future Improvements

- Conversation history
- Better search results
- Support for more documents
- User login
- Better answer formatting
- Error handling and logging
- Docker support
- CI/CD automation

---

## 📌 Project Status

✅ RAG pipeline implemented  
✅ Gemini embeddings integrated  
✅ Qdrant Cloud integrated  
✅ Semantic retrieval implemented  
✅ Relevance checking implemented  
✅ LangGraph workflow implemented  
✅ Streamlit frontend implemented  
✅ Source attribution implemented  
✅ Cloud deployment completed  

---

## 👩‍💻 Author

**Vraddhi Jain**