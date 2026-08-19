from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.rag.rag_pipeline import (
    retrieve_documents,
    generate_answer,
)


class RAGState(TypedDict):
    question: str
    results: list
    answer: str


def retrieve_node(state: RAGState):
#It performs retrieval.
    results = retrieve_documents(
        state["question"]
    )

    return {
        "results": results
    }


def generate_node(state: RAGState):
#It generates the answer.
    answer = generate_answer(
        state["question"],
        state["results"]
    )

    return {
        "answer": answer
    }


builder = StateGraph(RAGState)


builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "generate",
    generate_node
)


builder.add_edge(
    START,
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "generate"
)

builder.add_edge(
    "generate",
    END
)


rag_graph = builder.compile()