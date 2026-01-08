from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from .db import get_session, create_db
from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from .github_service import fetch_repo_data

router = APIRouter()

create_db()   # create tables when app starts


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate, session: Session = Depends(get_session)):

    repo_data = await fetch_repo_data(payload.github_repo)
    if repo_data is None:
        raise HTTPException(status_code=422, detail="Invalid GitHub repository")

    task = Task(
        title=payload.title,
        description=payload.description,
        github_repo=payload.github_repo,
        github_stars=repo_data["stars"],
        repo_description=repo_data["description"],
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: str, session: Session = Depends(get_session)):

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: str, payload: TaskUpdate, session: Session = Depends(get_session)):

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title:
        task.title = payload.title
    if payload.description:
        task.description = payload.description

    session.add(task)
    session.commit()
    session.refresh(task)

    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str, session: Session = Depends(get_session)):

    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()

    return None
