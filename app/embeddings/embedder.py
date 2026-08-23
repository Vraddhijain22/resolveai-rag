from langchain_ollama import OllamaEmbeddings

from app.config import EMBEDDING_MODEL


embeddings = OllamaEmbeddings(
    model=EMBEDDING_MODEL
)