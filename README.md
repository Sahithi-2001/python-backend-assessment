Project Structure

The project follows a simple layered structure to maintain separation of concerns:

app/ – Application source code

main.py – FastAPI app initialization

routes.py – API endpoint definitions

models.py – Database models

schemas.py – Pydantic request and response schemas

db.py – Database connection and session handling

github_service.py – External GitHub API integration logic

tests/ – Pytest-based test cases for API endpoints

requirements.txt – Project dependencies

.env.example – Example environment variables

README.md – Project documentation

This structure improves maintainability, readability, and testability.

Validation Logic

Request and response validation is handled using Pydantic schemas.
All incoming request data is validated before processing, ensuring required fields are present and correctly typed.

Response schemas ensure consistent API responses.
Invalid inputs automatically return appropriate 422 Unprocessable Entity errors.

External API Design

The GitHub REST API is used to fetch repository metadata such as star count and description.

No authentication is used (public GitHub API)

Asynchronous HTTP requests are made using httpx

External API failures are handled gracefully without breaking database integrity

Timeouts and unexpected responses are managed via exception handling

Solution Approach (Data Flow)

POST /tasks

Validate request payload using Pydantic

Call GitHub API to fetch repository details

Enrich task data with GitHub metadata

Store the task in PostgreSQL

Return the stored task as response

GET /tasks/{id}

Fetch task from database and return it

PUT /tasks/{id}

Update task fields and persist changes in database

DELETE /tasks/{id}

Remove task from database

Environment Variables

The project uses environment variables for configuration.

An example file is provided as .env.example containing:

DATABASE_URL

GITHUB_API_BASE

No real credentials are committed to the repository.
