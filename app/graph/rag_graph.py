from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.config import RELEVANCE_THRESHOLD

from app.rag.rag_pipeline import generate_answer
from app.vectorstore.search import search_documents


# ============================================================
# Constants
# ============================================================

INSUFFICIENT_MESSAGE = (
    "I couldn't find sufficient information in the "
    "available company knowledge base."
)


# ============================================================
# Graph State
# ============================================================

class RAGState(TypedDict):
    question: str
    results: list
    answer: str
    sources: list[dict]


# ============================================================
# Retrieve Node
# ============================================================

def retrieve_node(state: RAGState):

    results = search_documents(
        state["question"],
        top_k=1
    )

    return {
        "results": results
    }


# ============================================================
# Relevance Check Node
# ============================================================

def check_relevance_node(state: RAGState):

    relevant_results = [
        result
        for result in state["results"]
        if result.score >= RELEVANCE_THRESHOLD
    ]

    return {
        "results": relevant_results
    }


# ============================================================
# Conditional Routing
# ============================================================

def route_after_relevance(state: RAGState):

    if state["results"]:
        return "generate"

    return "reject"


# ============================================================
# Generate Answer Node
# ============================================================

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


# ============================================================
# Reject Node
# ============================================================

def reject_node(state: RAGState):

    return {
        "answer": INSUFFICIENT_MESSAGE,
        "sources": []
    }


# ============================================================
# Build LangGraph
# ============================================================

builder = StateGraph(RAGState)


# Add nodes

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


# ============================================================
# Graph Flow
# ============================================================

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


# ============================================================
# Compile Graph
# ============================================================

rag_graph = builder.compile()