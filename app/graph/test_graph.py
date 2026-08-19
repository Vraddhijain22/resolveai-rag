from app.graph.rag_graph import rag_graph


question = "How do I fix VPN after changing my password?"


result = rag_graph.invoke(
    {
        "question": question
    }
)


print("\n" + "=" * 70)
print("RESOLVEAI - LANGGRAPH TEST")
print("=" * 70)

print("\nQuestion:")
print(result["question"])

print("\nAnswer:")
print(result["answer"])