[![CI](https://github.com/csilva-intakedesk/api-tester/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)

# api-tester

Small FastAPI project with routes separated into categorized routers. This repo is intended as a local API test harness to emulate endpoints used by integrations.

## Contents

- `app/` — FastAPI application package
  - `main.py` — App bootstrap and router registration
  - `routers/` — Per-category routers (e.g. `litify.py`, `napoli.py`, etc.)
- `tests/` - FastAPI application tests
- `scripts/` — Helper scripts (e.g. `start_with_ngrok.sh`)
- `requirements.txt` — Minimal Python dependencies
- `pyproject.toml` - Project Definitions

## Requirements

- Python 3.9+ (3.10/3.11/3.12 supported)
- `pip` and a virtual environment tool (venv)

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # zsh / bash
python -m pip install --no-cache-dir -e '.[dev]'
```

## Run locally

The repository includes `scripts/start_with_ngrok.sh` which:

- Starts uvicorn on `127.0.0.1:8000` (with `--reload`).
- Waits for the `/healthz` endpoint to respond.
- Starts `ngrok http http://127.0.0.1:8000` and extracts the published public URL.
- Writes the public URL to `.logs/ngrok_url.txt` and prints it.
- Tails uvicorn and ngrok logs and cleans up both processes on exit.

Usage:

```bash
./scripts/start_with_ngrok.sh
```

Notes:

- Ensure `ngrok` is installed and on your PATH. To authenticate with your account, run `ngrok authtoken <token>`.
- The script uses the ngrok local API (`http://127.0.0.1:4040/api/tunnels`) to reliably get the public URL.

Health check:

```
GET http://127.0.0.1:8000/healthz
```

Interactive docs (Swagger UI):

```
http://127.0.0.1:8000/docs
```

## Development

If you are using vscode, please create a file to properly enable the best practices for the project.

```bash
code .vscode/settings.json
```

Add the following contents.

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.analysis.typeCheckingMode": "strict", // Pylance strict mode
  "ruff.enable": true,
  "ruff.organizeImports": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": { "source.fixAll": "explicit" }
}
```

## Available endpoints

Here’s a tighter, clearer version you can drop into your README:

> This service groups integration endpoints under the following routers: `/litify`, `/litify_czar`, `/napoli`, `/awko`, `/saddle`, `/smart_case_works`, and `/weitz`.

Each router typically exposes two core endpoints: **`/case`** and **`/document`**. Some integrations also provide **`/oauth`** for authorization flows.

Responses follow each partner’s specification and return either **JSON** (`application/json`) or **plain text** (often XML), with the appropriate `Content-Type` header.

A liveness probe is available at **`GET /healthz`**.

**Below is a summary of notable endpoints** (Method, Path, Short Description, Example):

- Health

  - GET `/healthz` — returns `{ "status": "ok" }`

- Litify router (`/litify`)

  - POST `/litify/case` — returns a JSON payload with `intakeId` and `message`.
    - Example: `curl -X POST http://127.0.0.1:8000/litify/case`
  - POST `/litify/xml` — returns an XML string matching the PHP-style output.
    - Accepts JSON body `{ "reqId": "..." }` (optional). If not provided, server generates a token.
    - Example:
      ```bash
      curl -X POST -H "Content-Type: application/json" -d '{"reqId": "12345"}' \
      	http://127.0.0.1:8000/litify/xml
      # <?xml version="1.0" encoding="utf-8"?>OK 12345
      ```

- Napoli router (`/napoli`)

  - Multiple POST endpoints that return sample JSON payloads used by integrations. Notable ones:
    - POST `/napoli/EmergencyContact` — returns a sample emergency contact payload.
    - POST `/napoli/EmergencyContact/{sysid}` — returns the same payload but with the provided `sysid` value inserted.
      - Example:
        ```bash
        curl -X POST http://127.0.0.1:8000/napoli/EmergencyContact/C66B7E02D466ACF4
        ```
    - POST `/napoli/GetNewSysId` — returns a detailed sample payload including `SYSID`.

- Other routers
  - `/litify_czar`, `/awko`, `/saddle`, `/smart_case_works`, `/weitz` — each file under `app/routers/` contains stub endpoints that return representative sample payloads. Browse the code or use the interactive docs to view and test them.

## Response types

- JSON responses are returned as `application/json` via `JSONResponse`.
- Some endpoints return plain text or XML; those use `Response(..., media_type=...)` - Text Response

## Example testing commands

- Test health:

  ```bash
  curl -i http://127.0.0.1:8000/healthz
  ```

- Test litify JSON intake:

  ```bash
  curl -X POST http://127.0.0.1:8000/litify/case
  ```

- Test litify XML:

  ```bash
  curl -X POST http://127.0.0.1:8000/smart_case_works/document
  ```

- Test napoli emergency contact with sysid:
  ```bash
  curl -X POST http://127.0.0.1:8000/napoli/EmergencyContact/C66B7E02D466ACF4
  ```

## Troubleshooting

- If imports fail in your editor (e.g. "Import fastapi could not be resolved"), ensure your editor is using the same Python interpreter where you installed dependencies (the `.venv` interpreter).
- If `ngrok` fails to start or the local API is not reachable, check `~/.ngrok2` auth or run `ngrok http 8000` manually to inspect logs.

## Extending the project

- Add new routers under `app/routers/` as `*.py` files exposing an `APIRouter` named `router`.
- Register the new router in `app/main.py` by adding to the `routers = [...]` list.
- Add tests under a `tests/` directory (pytest) if you want CI coverage.

## License

Proprietary & Confidential — IntakeDesk LLC

This software and its documentation are the confidential and proprietary property of IntakeDesk LLC.
No rights are granted except as expressly authorized in a written agreement with IntakeDesk LLC.
You may not copy, modify, distribute, sublicense, or reverse-engineer any part of this code
except as permitted by law or contract. Provided “AS IS” without warranties of any kind.
