from app.graph.rag_graph import rag_graph


print("\n" + "=" * 70)
print("RESOLVEAI - LANGGRAPH KNOWLEDGE ASSISTANT")
print("=" * 70)

print("\nType 'exit' to quit.")


while True:

    question = input("\nAsk your question: ").strip()


    if question.lower() == "exit":

        print("\nGoodbye!")

        break


    if not question:

        print("Please enter a question.")

        continue


    result = rag_graph.invoke(
        {
            "question": question,
            "results": [],
            "answer": "",
            "sources": []
        }
    )


    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)

    print(result["answer"])


    if result["sources"]:

        print("\n" + "=" * 70)
        print("SOURCES")
        print("=" * 70)

        for source in result["sources"]:

            print(f"- {source}")