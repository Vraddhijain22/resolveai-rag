from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.config import RELEVANCE_THRESHOLD

from app.rag.rag_pipeline import (
    retrieve_documents,
    generate_answer,
)


INSUFFICIENT_MESSAGE = (
    "I couldn't find sufficient information in the "
    "available company knowledge base."
)


class RAGState(TypedDict):
    question: str
    results: list
    answer: str
    sources: list[dict]


def retrieve_node(state: RAGState):

    results = retrieve_documents(
        state["question"]
    )

    return {
        "results": results
    }


def check_relevance_node(state: RAGState):

    relevant_results = [
        result
        for result in state["results"]
        if result.score >= RELEVANCE_THRESHOLD
    ]

    return {
        "results": relevant_results
    }


def route_after_relevance(state: RAGState):

    if state["results"]:
        return "generate"

    return "reject"


def generate_node(state: RAGState):

    answer = generate_answer(
        state["question"],
        state["results"]
    )

    sources = []

    if answer.strip() != INSUFFICIENT_MESSAGE:

        for result in state["results"]:

            source = {
                "document": result.payload["source"],
                "page": result.payload["page"],
                "score": round(result.score, 4)
            }

            if source not in sources:
                sources.append(source)

    return {
        "answer": answer,
        "sources": sources
    }


def reject_node(state: RAGState):

    return {
        "answer": INSUFFICIENT_MESSAGE,
        "sources": []
    }


builder = StateGraph(RAGState)


builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "check_relevance",
    check_relevance_node
)

builder.add_node(
    "generate",
    generate_node
)

builder.add_node(
    "reject",
    reject_node
)


builder.add_edge(
    START,
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "check_relevance"
)

builder.add_conditional_edges(
    "check_relevance",
    route_after_relevance,
    {
        "generate": "generate",
        "reject": "reject",
    }
)

builder.add_edge(
    "generate",
    END
)

builder.add_edge(
    "reject",
    END
)


rag_graph = builder.compile()