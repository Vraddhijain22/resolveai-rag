from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.graph.rag_graph import rag_graph


app = FastAPI(
    title="ResolveAI",
    description="AI-powered enterprise knowledge assistant",
    version="1.0.0"
)


# Allow the frontend to communicate with the API.
# This is open during local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    try:

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

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail="Unable to process the question."
        ) from error