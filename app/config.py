from pathlib import Path


# Project paths

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_FOLDER = BASE_DIR / "data" / "documents"

VECTORSTORE_FOLDER = BASE_DIR / "data" / "qdrant"


# Ollama models

LLM_MODEL = "qwen2.5:3b"

EMBEDDING_MODEL = "nomic-embed-text"


# Qdrant

COLLECTION_NAME = "policy_documents"

VECTOR_SIZE = 768


# RAG

RELEVANCE_THRESHOLD = 0.60