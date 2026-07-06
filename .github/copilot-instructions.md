# Copilot Instructions for ha-api

## Project Overview
A Flask-based API for Home Assistant integration that handles Google Sheets operations, specifically solar immersion data logging. The API exposes endpoints secured with secrets and integrates with Google Sheets via service account authentication.

## Tech Stack
- **Runtime**: Python 3.13+
- **Framework**: Flask 3.1.3
- **Dependency Manager**: `uv` (modern, fast Python package manager)
- **Google Integration**: gspread, google-auth for Sheets API
- **Deployment**: Docker (Alpine base, uv runtime)
- **Host**: 0.0.0.0:5000

## Project Structure
```
ha-api/
├── ha_api/
│   ├── __init__.py          # Flask app initialization
│   └── routes.py            # API endpoints (immersion, etc.)
├── include/
│   ├── google_sheets.py     # Spreadsheet class & Google Sheets operations
│   └── logger.py            # Logging utility
├── run.py                   # Entry point (app.run)
├── Dockerfile               # Alpine base with uv
├── docker-compose.yml       # Service definition with volumes
└── pyproject.toml           # Project metadata & dependencies
```

## Build & Run
- **Development**: `uv run python run.py` or `python -m flask --app run run --host=0.0.0.0`
- **Docker**: `docker-compose up --build`
- **Dependencies**: Managed via `uv sync` (installed in Dockerfile)

## Code Conventions
1. **Imports**: Follow Python stdlib → third-party → local pattern
2. **Route Security**: Use query parameter secrets (e.g., `?secret=...`) for endpoint protection
3. **Google Sheets**: Credentials mounted at `/app/google.json` (volume mount in docker-compose)
4. **Logging**: Use include.logger.log for debug/info messages
5. **Timezone**: Helper functions use local system time (local_time_now)
6. **Date Formatting**: ISO format for consistency (YYYY-MM-DD HH:MM:SS)

## Common Development Tasks
- **Add new endpoint**: Edit `ha_api/routes.py`, import necessary utilities, secure with secret parameter
- **Update Google Sheets interaction**: Modify `include/google_sheets.py` Spreadsheet class
- **Add dependencies**: Update `pyproject.toml`, run `uv sync`
- **Build Docker image**: `docker-compose build`
- **Check running container**: `docker ps` to find `ha-api` container

## Potential Issues & Considerations
- **Google credentials**: `/app/google.json` must be present at runtime (volume mount required)
- **Port conflicts**: Flask runs on 5000 by default; docker-compose maps to host 5000
- **Debug mode**: Currently disabled in run.py (production setting)
- **uv vs pip**: Always use `uv` for package operations, not pip
- **Hardcoded paths**: Paths like `/app/google.json` are containerized; adjust for local dev if needed

## Testing
No test suite currently visible. Consider adding pytest for:
- Endpoint response validation
- Google Sheets integration mocking
- Date formatting edge cases

## Key Files to Know
- [run.py](run.py) - Application entry point
- [ha_api/__init__.py](ha_api/__init__.py) - Flask app factory & route import
- [ha_api/routes.py](ha_api/routes.py) - All API endpoint definitions
- [include/google_sheets.py](include/google_sheets.py) - Spreadsheet operations
- [Dockerfile](Dockerfile) - Container build steps
