from qdrant_client import QdrantClient
from langchain_ollama import ChatOllama

from app.config import (
    VECTORSTORE_FOLDER,
    COLLECTION_NAME,
    RELEVANCE_THRESHOLD,
    LLM_MODEL,
)

from app.embeddings.embedder import embeddings


llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0
)


def retrieve_documents(
    question: str,
    top_k: int = 3
):

    client = QdrantClient(
        path=VECTORSTORE_FOLDER
    )

    try:

        query_vector = embeddings.embed_query(
            question
        )

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=top_k
        ).points

        return results

    finally:

        client.close()


def generate_answer(
    question: str,
    results
):

    relevant_results = [
        result
        for result in results
        if result.score >= RELEVANCE_THRESHOLD
    ]


    if not relevant_results:

        return (
            "I couldn't find sufficient information in the "
            "available company knowledge base."
        )


    context_parts = []


    for result in relevant_results:

        context_parts.append(
            f"""
Document: {result.payload['source']}
Page: {result.payload['page']}

{result.payload['text']}
"""
        )


    context = "\n".join(context_parts)


    prompt = f"""
You are ResolveAI, an enterprise knowledge assistant.

Answer the user's question ONLY using the provided company knowledge.

Do not use outside knowledge.

Do not guess or invent information.

If the provided knowledge does not contain enough information
to answer the question, say:

"I couldn't find sufficient information in the available company knowledge base."

Keep the answer clear and concise.

AVAILABLE COMPANY KNOWLEDGE:

{context}

END OF COMPANY KNOWLEDGE.

USER QUESTION:

{question}

ANSWER:
"""


    response = llm.invoke(prompt)

    return response.content


def ask_question(
    question: str
):

    results = retrieve_documents(
        question
    )

    answer = generate_answer(
        question,
        results
    )

    return answer, results