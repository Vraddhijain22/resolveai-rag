from app.embeddings.embedder import embeddings


text = "Employees must submit travel expenses within 15 calendar days."


vector = embeddings.embed_query(text)


print("Text:")
print(text)

print("\nEmbedding length:")
print(len(vector))

print("\nFirst 10 values:")
print(vector[:10])