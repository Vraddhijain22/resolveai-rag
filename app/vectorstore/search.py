import time

from qdrant_client import QdrantClient

from app.config import (
    VECTORSTORE_FOLDER,
    COLLECTION_NAME,
)

from app.embeddings.embedder import embeddings


def search_documents(
    query: str,
    top_k: int = 3,
    max_retries: int = 3
):
    """
    Search the Qdrant vector store using Gemini embeddings.

    Retries the embedding request if Gemini temporarily
    returns a rate-limit (429) error.
    """

    query_vector = None

    for attempt in range(max_retries):

        try:

            query_vector = embeddings.embed_query(
                query
            )

            break

        except Exception as error:

            if "429" not in str(error):

                raise

            if attempt == max_retries - 1:

                raise

            wait_time = 5 * (attempt + 1)

            print(
                f"Gemini rate limit reached. "
                f"Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)

    client = QdrantClient(
        path=str(VECTORSTORE_FOLDER)
    )

    try:

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=top_k
        ).points

        return results

    finally:

        client.close()