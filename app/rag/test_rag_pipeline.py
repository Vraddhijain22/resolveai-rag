from app.rag.rag_pipeline import ask_question


print("\n" + "=" * 70)
print("RESOLVEAI - ENTERPRISE KNOWLEDGE ASSISTANT")
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


    answer, results = ask_question(
        question
    )


    print("\n" + "=" * 70)
    print("ANSWER")
    print("=" * 70)

    print(answer)


    relevant_sources = []


    for result in results:

        if result.score >= 0.60:

            source = (
                f"{result.payload['source']}, "
                f"Page {result.payload['page']}"
            )

            if source not in relevant_sources:

                relevant_sources.append(source)


    # Show sources only when the answer is based on company knowledge.
if (
    answer !=
    "I couldn't find sufficient information in the available company knowledge base."
    and relevant_sources
):

    print("\n" + "=" * 70)
    print("SOURCES")
    print("=" * 70)

    for source in relevant_sources:

        print(f"- {source}")