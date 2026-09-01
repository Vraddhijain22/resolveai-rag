from pathlib import Path
import os


# ============================================================
# Project paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_FOLDER = BASE_DIR / "data" / "documents"

VECTORSTORE_FOLDER = BASE_DIR / "data" / "qdrant"


# ============================================================
# Models
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
# Qdrant
# ============================================================

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "policy_documents"
)

VECTOR_SIZE = int(
    os.getenv(
        "VECTOR_SIZE",
        "768"
    )
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