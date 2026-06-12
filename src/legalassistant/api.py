from fastapi import FastAPI
from pydantic import BaseModel
import json

from legalassistant.crew import LegalAssistant

app= FastAPI(
    title="AI Legal Assistant API",
    description="API for the AI Legal Assistant Crew",
    version="1.0.0"
)

class LegalRequest(BaseModel):
    user_input: str
    
    
@app.get("/")
def root():
    return {
        "message": "AI Legal Assistant API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(request: LegalRequest):

    result = LegalAssistant().crew().kickoff(
        inputs={
            "user_input": request.user_input
        }
    )

    return {
        "case_summary": result.tasks_output[0].raw,
        "ipc_sections": json.loads(result.tasks_output[1].raw),
        "precedents": result.tasks_output[2].raw,
        "legal_document": result.tasks_output[3].raw
    }


