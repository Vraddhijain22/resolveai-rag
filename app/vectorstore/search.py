from qdrant_client import QdrantClient

from app.embeddings.embedder import embeddings


VECTORSTORE_FOLDER = "data/qdrant"

COLLECTION_NAME = "policy_documents"


client = QdrantClient(
    path=VECTORSTORE_FOLDER
)


# query = "How long do I have to submit my travel expenses?"
query = "What should I do if I clicked a suspicious phishing link?"
query_vector = embeddings.embed_query(query)


results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vector,
    limit=3
).points


print("\n" + "=" * 70)
print("SEARCH QUERY")
print("=" * 70)

print(query)


print("\n" + "=" * 70)
print("SEARCH RESULTS")
print("=" * 70)


for index, result in enumerate(results, start=1):

    print(f"\nResult {index}")
    print("-" * 70)

    print(f"Score: {result.score}")

    print(f"Source: {result.payload['source']}")

    print(f"Page: {result.payload['page']}")

    print("\nText:")

    print(result.payload["text"])


# Explicitly close Qdrant before the program exits
client.close()