from pydantic import BaseModel, field_validator
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str
    github_repo: str   # example: owner/repo

    @field_validator("github_repo")
    @classmethod
    def validate_repo(cls, value):
        if "/" not in value:
            raise ValueError("Repository must be in format owner/repo")
        return value


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    github_repo: str
    github_stars: int
    repo_description: Optional[str]
