from qdrant_client import QdrantClient

from app.config import (
    COLLECTION_NAME,
    QDRANT_URL,
    QDRANT_API_KEY,
)

from app.embeddings.embedder import embeddings


# ============================================================
# QDRANT CLOUD CLIENT
# ============================================================

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)


# ============================================================
# SEARCH DOCUMENTS
# ============================================================

def search_documents(
    query: str,
    top_k: int = 3,
):

    query_vector = embeddings.embed_query(
        query
    )

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
    ).points

    return results