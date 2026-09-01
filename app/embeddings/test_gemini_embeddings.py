from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import (
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
)


embeddings = GoogleGenerativeAIEmbeddings(
    model=GEMINI_EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY,
)


text = "How long do I have to submit my travel expenses?"

vector = embeddings.embed_query(text)


print("\n" + "=" * 70)
print("GEMINI EMBEDDING TEST")
print("=" * 70)

print("\nModel:")
print(GEMINI_EMBEDDING_MODEL)

print("\nVector dimension:")
print(len(vector))

print("\nFirst 5 values:")
print(vector[:5])