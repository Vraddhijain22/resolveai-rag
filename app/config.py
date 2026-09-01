from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# ============================================================
# Project paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_FOLDER = BASE_DIR / "data" / "documents"

VECTORSTORE_FOLDER = BASE_DIR / "data" / "qdrant"


# ============================================================
# Providers
# ============================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama"
)

EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER",
    "ollama"
)

VECTORSTORE_PROVIDER = os.getenv(
    "VECTORSTORE_PROVIDER",
    "local"
)


# ============================================================
# Local Ollama models
# ============================================================

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen2.5:3b"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "nomic-embed-text"
)


# ============================================================
# Gemini
# ============================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
)

GEMINI_LLM_MODEL = os.getenv(
    "GEMINI_LLM_MODEL",
    "gemini-3.6-flash"
)

GEMINI_EMBEDDING_MODEL = os.getenv(
    "GEMINI_EMBEDDING_MODEL",
    "gemini-embedding-001"
)


# ============================================================
# Qdrant
# ============================================================

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "policy_documents"
    if EMBEDDING_PROVIDER == "ollama"
    else "policy_documents_gemini"
)

VECTOR_SIZE = int(
    os.getenv(
        "VECTOR_SIZE",
        "768" if EMBEDDING_PROVIDER == "ollama" else "3072"
    )
)

QDRANT_URL = os.getenv(
    "QDRANT_URL",
    ""
)

QDRANT_API_KEY = os.getenv(
    "QDRANT_API_KEY",
    ""
)


# ============================================================
# RAG
# ============================================================

RELEVANCE_THRESHOLD = float(
    os.getenv(
        "RELEVANCE_THRESHOLD",
        "0.60"
    )
)