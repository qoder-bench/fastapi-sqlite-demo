# FastAPI SQLite demo

## Tech Stack

- Python 3.13
- Project/Package Manager: [uv](https://docs.astral.sh/uv)
- Web Framework: FastAPI
- Database: SQLite
- ORM: SQLModel with async support
- Testing: pytest
- Linter: [ruff](https://github.com/astral-sh/ruff)
- type checker: [ty](https://github.com/astral-sh/ty)

## Project structure

- `db/demo.sqlite3`: SQLite database file
- `db/schema.ddl`: database schema
- `app/`: Main application code
    - `main.py`: Entry point of the application
    - `routers/`: API route definitions
    - `domains/`: Domain related code
        - `models.py`: SQLModel models
        - `repository/`: Repository layer
        - `infra`: Infrastructure layer
- `tests/`: integration test for the application

For unit test, please put them in `tests/` subdirectory.

## Build

The project uses [just](https://github.com/casey/just) as task runner.

- Start server: `just start`
- Generate SQLModels: `just gen-sqlmodels`

## Configurations

The project use `.env` file to store configurations.