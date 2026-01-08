# Python Backend Engineer Take Home Assessment

## Overview
This project implements a REST API service using **FastAPI** and **PostgreSQL**.  
The service acts as a bridge between a local database and an external API (**GitHub**), enriching stored data with repository metadata such as star count and description.

---

## Problem Understanding & Use Case

### Interpretation
The goal of this assessment was to build a robust backend service that:
- Exposes REST APIs using FastAPI
- Persists data in PostgreSQL
- Integrates with an external API
- Applies strict request and response validation
- Includes automated testing and clear documentation

### Use Case
**GitHub Task Tracker**  
Users can create tasks linked to GitHub repositories.  
When a task is created, repository details are fetched from GitHub and stored along with the task.

### Assumptions
- No user authentication is required.
- GitHub public API is available and reliable.
- The application is designed for single-user usage.
- External API failures should not corrupt database state.

---

## Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLModel
- Pydantic
- Pytest

---

## API Endpoints
- **POST /tasks** – Create a task with GitHub repository enrichment
- **GET /tasks/{id}** – Fetch a task by ID
- **PUT /tasks/{id}** – Update an existing task
- **DELETE /tasks/{id}** – Delete a task

---

## Project Structure

The project follows a layered structure to ensure separation of concerns:

- `app/`
  - `main.py` – FastAPI application entry point
  - `routes.py` – API route definitions
  - `models.py` – Database models
  - `schemas.py` – Pydantic request and response schemas
  - `db.py` – Database connection and session handling
  - `github_service.py` – External GitHub API integration
- `tests/` – Pytest-based test cases
- `requirements.txt` – Project dependencies
- `.env.example` – Example environment variables
- `README.md` – Project documentation

---

## Database Design
A single `tasks` table is used to store:
- Task details (title, description)
- GitHub repository name
- Repository star count
- Repository description

A simple schema was chosen to keep the design minimal and efficient for the use case.

---

## Validation Logic
All request and response validation is handled using **Pydantic** schemas.

- Required fields are enforced
- Invalid data types automatically return `422 Unprocessable Entity`
- Response schemas ensure consistent API responses

---

## External API Design
The GitHub REST API is used to fetch repository metadata.

- Public GitHub API (no authentication required)
- Asynchronous HTTP requests using `httpx`
- External API failures are handled gracefully
- Errors do not affect database consistency

---

## Solution Approach (Data Flow)

### POST /tasks
1. Validate request payload using Pydantic
2. Call GitHub API to fetch repository details
3. Enrich task data with GitHub metadata
4. Store the task in PostgreSQL
5. Return the created task as response

### GET /tasks/{id}
- Fetch the task from database and return it

### PUT /tasks/{id}
- Update task fields and persist changes in database

### DELETE /tasks/{id}
- Remove the task from database

---

## Error Handling Strategy
- Global FastAPI exception handler is implemented
- Database and external API failures are handled gracefully
- Appropriate HTTP status codes are returned
- Internal errors are not exposed to clients

---

## How to Run the Project

### Setup
1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt

2.Ensure PostgreSQL is running and the database exists.

3.Start the server:

python -m uvicorn app.main:app --reload


4.Open Swagger documentation:

http://127.0.0.1:8000/docs

Environment Variables

An example environment configuration is provided in .env.example.

DATABASE_URL

GITHUB_API_BASE

No real credentials are committed to the repository.

### Testing

Tests are implemented using Pytest.

### Notes

Docker was not used as it was optional.
The focus was placed on correctness, validation, testing, and documentation clarity.

Run all tests:

pytest -q
