from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid


class Task(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    description: str
    github_repo: str
    github_stars: int = 0
    repo_description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
