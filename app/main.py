from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.graph.rag_graph import rag_graph


app = FastAPI(
    title="ResolveAI",
    description="AI-powered enterprise knowledge assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question to ask the enterprise knowledge assistant"
    )


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[str]


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


@app.post(
    "/ask",
    response_model=AskResponse
)
def ask_question(request: QuestionRequest):

    result = rag_graph.invoke(
        {
            "question": request.question,
            "results": [],
            "answer": "",
            "sources": []
        }
    )

    return AskResponse(
        question=request.question,
        answer=result["answer"],
        sources=result["sources"]
    )