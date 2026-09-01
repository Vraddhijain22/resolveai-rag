from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from app.config import (
    VECTORSTORE_FOLDER,
    COLLECTION_NAME,
    QDRANT_URL,
    QDRANT_API_KEY,
)


LOCAL_COLLECTION = "policy_documents_gemini"
CLOUD_COLLECTION = COLLECTION_NAME


# ============================================================
# CLIENTS
# ============================================================

local_client = QdrantClient(
    path=str(VECTORSTORE_FOLDER)
)

cloud_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)


# ============================================================
# READ LOCAL VECTORS
# ============================================================

print("=" * 70)
print("READING LOCAL GEMINI VECTORS")
print("=" * 70)

local_info = local_client.get_collection(
    LOCAL_COLLECTION
)

print(
    f"Local vectors: {local_info.points_count}"
)


points, _ = local_client.scroll(
    collection_name=LOCAL_COLLECTION,
    limit=100,
    with_payload=True,
    with_vectors=True,
)

print(
    f"Points retrieved: {len(points)}"
)


# ============================================================
# PREPARE POINTS
# ============================================================

cloud_points = []

for point in points:

    cloud_points.append(
        PointStruct(
            id=point.id,
            vector=point.vector,
            payload=point.payload,
        )
    )


# ============================================================
# UPLOAD
# ============================================================

print("\nUploading vectors to Qdrant Cloud...")

if cloud_points:

    cloud_client.upsert(
        collection_name=CLOUD_COLLECTION,
        points=cloud_points,
        wait=True,
    )

    print(
        f"Uploaded: {len(cloud_points)}"
    )

else:

    print("No vectors found!")


# ============================================================
# VERIFY
# ============================================================

print("\n" + "=" * 70)
print("VERIFYING CLOUD")
print("=" * 70)

info = cloud_client.get_collection(
    CLOUD_COLLECTION
)

print(
    f"Cloud vectors: {info.points_count}"
)


local_client.close()
cloud_client.close()