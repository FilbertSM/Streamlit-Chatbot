from pydantic import BaseModel, Field
from typing import List
from beanie import Document

class ValidationRow(BaseModel):
    criteria: str = Field(..., description="The specific skill being graded")
    evidence: str = Field(..., description="Direct quote from the trainee's chat that proves this skill")
    justification: str = Field(..., description="Reasoning why the evidence meets the criteria")
    score: int = Field(..., description="A score from 0 to 100")

class AssessmentResult(BaseModel):
    grading_table: List[ValidationRow] = Field(..., description="All the rows in ValidationRow Scheme")
    overall_summary: str = Field(..., description="Overall summary of the Roleplay Session")
    final_grade: int = Field(..., description="Final score of the session from 0 to 100")

class TrainingSession(Document):
    chat_history: List[dict]