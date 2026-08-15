from fastapi import FastAPI

app = FastAPI(
    title="PolicyBot",
    description="AI-powered policy knowledge assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "PolicyBot API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }