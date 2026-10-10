
from fastapi import FastAPI

from backend.schemas import ScanRequest, ScanResponse
from backend.agent import scan_with_agent


app = FastAPI(
    title="AgentShield AI",
    description="AI-Powered Prompt Injection Firewall",
    version="1.1.0",
)


@app.get("/")
def home():
    return {
        "project": "AgentShield AI",
        "message": "AgentShield Firewall Running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/scan", response_model=ScanResponse)
def scan_prompt(request: ScanRequest):
    return scan_with_agent(request.prompt)
