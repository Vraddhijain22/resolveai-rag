from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.config import (
    DOCUMENTS_FOLDER,
    VECTORSTORE_FOLDER,
    COLLECTION_NAME,
    VECTOR_SIZE,
)

from app.embeddings.embedder import embeddings
from app.rag.document_loader import load_pdf
from app.rag.chunker import chunk_text


pdf_files = list(DOCUMENTS_FOLDER.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF documents.")


client = QdrantClient(
    path=str(VECTORSTORE_FOLDER)
)


if not client.collection_exists(COLLECTION_NAME):

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )

    print(f"Created collection: {COLLECTION_NAME}")

else:

    print(f"Collection already exists: {COLLECTION_NAME}")


all_chunks = []


for pdf_file in pdf_files:

    print("\n" + "=" * 70)
    print(f"Processing: {pdf_file.name}")

    pages = load_pdf(str(pdf_file))

    print(f"Pages extracted: {len(pages)}")

    for page in pages:

        chunks = chunk_text(page["text"])

        for chunk in chunks:

            all_chunks.append({
                "text": chunk,
                "source": page["source"],
                "page": page["page"]
            })


print("\n" + "=" * 70)
print(f"Total chunks created: {len(all_chunks)}")


print("\nCreating embeddings...")


for index, chunk in enumerate(all_chunks):

    print(
        f"Embedding chunk {index + 1}/{len(all_chunks)}"
    )

    vector = embeddings.embed_query(
        chunk["text"]
    )

    point = PointStruct(
        id=index,
        vector=vector,
        payload={
            "text": chunk["text"],
            "source": chunk["source"],
            "page": chunk["page"]
        }
    )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[point]
    )


print("\n" + "=" * 70)
print("Vector store creation completed successfully.")


collection_info = client.get_collection(
    COLLECTION_NAME
)

print(
    f"Vectors stored: {collection_info.points_count}"
)