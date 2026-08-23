from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.rag_graph import rag_graph


app = FastAPI(
    title="ResolveAI",
    description="AI-powered enterprise knowledge assistant",
    version="1.0.0"
)


class QuestionRequest(BaseModel):

    question: str


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


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = rag_graph.invoke(
        {
            "question": request.question,
            "results": [],
            "answer": "",
            "sources": []
        }
    )

    return {
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }