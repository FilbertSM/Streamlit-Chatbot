from pydantic import BaseModel, Field
from typing import List
from beanie import Document
from datetime import datetime, timezone, timedelta

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

# User Models
class User(Document):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the user")
    password: str = Field(..., description="Password of the user")

    class Settings:
        collection_name="users"
    
class UserRegister(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the user")
    password: str = Field(..., description="Password of the user")
    confirm_password: str = Field(..., description="Confirmation Password")

class Login(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="Name of the user")
    password: str = Field(..., description="Password of the user")

# Message Models
class Message(Document):
    role: str = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")
    timezone_jkt = timezone(timedelta(hours=7))
    created_at: datetime = datetime.now(tz=timezone_jkt)

    class Settings:
        collection_name="messages"

class Message(BaseModel):
    role: str = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")