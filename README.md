# Python Backend Engineer Take Home Assessment

## Overview
This project implements a REST API using FastAPI and PostgreSQL.  
The service acts as a bridge between a local database and an external API (GitHub), enriching stored data with repository metadata.

## Use Case
GitHub Task Tracker – tasks are created with GitHub repository references, and repository details such as star count and description are fetched and stored.

## Assumptions
- No authentication is required.
- GitHub public API is available and reliable.
- Single-user usage.
- External API failures should not corrupt database state.

## Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLModel
- Pydantic
- Pytest

## API Endpoints
- POST /tasks – Create task with GitHub repo enrichment
- GET /tasks/{id} – Fetch task
- PUT /tasks/{id} – Update task
- DELETE /tasks/{id} – Delete task

## Database Design
Single `tasks` table storing task metadata along with GitHub repository details.

## External API Integration
GitHub REST API is used to fetch repository information such as stars and description using async HTTP requests.

## Error Handling
- Global exception handler implemented.
- Graceful handling of database and external API failures.
- Proper HTTP status codes returned.

## How to Run
1. Install dependencies:

python -m pip install -r requirements.txt

2. Ensure PostgreSQL is running and database exists.
3. Start server:
python -m uvicorn app.main:app --reload

4. Open Swagger docs:
http://127.0.0.1:8000/docs

## Testing
Run tests using:
pytest -q
## Notes
Docker was not used as it was optional. Focus was placed on correctness, validation, testing, and documentation clarity.
