from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import (
    EMBEDDING_PROVIDER,
    EMBEDDING_MODEL,
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
)


if EMBEDDING_PROVIDER == "ollama":

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )


elif EMBEDDING_PROVIDER == "gemini":

    embeddings = GoogleGenerativeAIEmbeddings(
        model=GEMINI_EMBEDDING_MODEL,
        google_api_key=GEMINI_API_KEY,
    )


else:

    raise ValueError(
        f"Unsupported embedding provider: {EMBEDDING_PROVIDER}"
    )