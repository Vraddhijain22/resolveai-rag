from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.graph.rag_graph import rag_graph


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="ResolveAI",
    description="AI-powered enterprise knowledge assistant",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

# Open CORS for local frontend development.
# This will be restricted before production deployment.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Request / Response Models
# ============================================================

class QuestionRequest(BaseModel):

    question: str = Field(
        ...,
        min_length=1,
        description="Question to ask the enterprise knowledge assistant"
    )


class Source(BaseModel):

    document: str
    page: int
    score: float


class AskResponse(BaseModel):

    question: str
    answer: str
    sources: list[Source]


# ============================================================
# Health / Root Endpoints
# ============================================================

@app.get("/")
def root():

    return {
        "message": "ResolveAI API is running!"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ============================================================
# Ask Endpoint
# ============================================================

@app.post(
    "/ask",
    response_model=AskResponse
)
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:

        result = rag_graph.invoke(
            {
                "question": question,
                "results": [],
                "answer": "",
                "sources": []
            }
        )

        return AskResponse(
            question=question,
            answer=result["answer"],
            sources=result["sources"]
        )

    except Exception as error:

        print(
            f"Error processing question: {error}"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process the question."
        ) from error