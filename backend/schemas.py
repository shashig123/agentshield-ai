
from pydantic import BaseModel, Field
from typing import List, Literal


class ScanRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=10000)


class ScanResponse(BaseModel):
    prompt: str
    decision: Literal["ALLOW", "BLOCK", "REVIEW"]
    risk_level: Literal["LOW", "MEDIUM", "HIGH", "UNKNOWN"]
    attack_types: List[str]
    explanation: str
    detected_patterns: List[str]
    model_used: str | None = None
    analysis_steps: List[str] = Field(default_factory=list)
    ai_error: str | None = None
