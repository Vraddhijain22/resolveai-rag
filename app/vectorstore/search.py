from qdrant_client import QdrantClient

from app.config import (
    VECTORSTORE_FOLDER,
    COLLECTION_NAME,
)

from app.embeddings.embedder import embeddings


# ============================================================
# Search Configuration
# ============================================================

QUERY = "What should I do if I clicked a suspicious phishing link?"

TOP_K = 3


# ============================================================
# Qdrant Search
# ============================================================

client = QdrantClient(
    path=VECTORSTORE_FOLDER
)

try:

    query_vector = embeddings.embed_query(
        QUERY
    )

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=TOP_K
    ).points

finally:

    client.close()


# ============================================================
# Display Results
# ============================================================

print("\n" + "=" * 70)
print("SEARCH QUERY")
print("=" * 70)

print(QUERY)


print("\n" + "=" * 70)
print("SEARCH RESULTS")
print("=" * 70)


for index, result in enumerate(results, start=1):

    print(f"\nResult {index}")
    print("-" * 70)

    print(
        f"Score: {result.score:.4f}"
    )

    print(
        f"Source: {result.payload['source']}"
    )

    print(
        f"Page: {result.payload['page']}"
    )

    print("\nText:")

    print(
        result.payload["text"]
    )