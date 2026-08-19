# ResolveAI — Enterprise Knowledge Assistant

ResolveAI is an AI-powered enterprise knowledge assistant built using Retrieval-Augmented Generation (RAG).

The system is designed to help employees find answers from internal company policies, SOPs, and troubleshooting documentation.

## Problem

Employees often need to search through multiple internal documents to find answers about:

- IT troubleshooting
- Password management
- Travel reimbursement
- Expense approval
- Remote work policies
- Security and phishing procedures

ResolveAI aims to provide a conversational interface that retrieves relevant company information and generates grounded answers.

## Current Tech Stack

- Python
- FastAPI
- LangChain
- Ollama
- Qwen 2.5 3B
- PyPDF
- Git
- GitHub

## Current Pipeline

PDF Documents
    ↓
Document Ingestion
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Prompt + Context
    ↓
Qwen 2.5 3B
    ↓
Grounded Response

## Current Features

- PDF document ingestion
- Multi-document processing
- PDF text extraction
- Page and source metadata
- Text chunking
- Chunk overlap
- Local LLM inference
- LangChain integration
- Prompt engineering
- Basic grounding and hallucination testing

## Planned Features

- Embedding generation
- Vector database using Qdrant
- Semantic search
- Top-K retrieval
- Retrieval evaluation
- RAG evaluation
- LangGraph workflow
- Query rewriting
- Retrieval validation
- Citation generation
- FastAPI API
- Streamlit frontend
- Docker
- Cloud deployment
- CI/CD

## Project Architecture

Coming soon.

## Project Status

🚧 Work in progress.

This project is being built as a practical AI/LLM engineering portfolio project.