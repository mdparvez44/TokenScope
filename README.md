# TokenScope

TokenScope is a **local‑first** developer tool for inspecting, profiling, and diagnosing the context sent to large language models (LLMs). It provides:

- Token counts and context‑window utilization
- Categorisation of messages (system, user, assistant, tool, RAG, …)
- A visual minimap of where each segment lives in the request
- Diagnostics for oversized or duplicated content
- Privacy‑first design – all analysis runs locally, no telemetry.

## Repository layout (Phase 1)
```
TokenScope/
├─ sdk/                # pure‑Python SDK & core engine
│   ├─ pyproject.toml
│   └─ src/
│       └─ tokenscope/
│           ├─ __init__.py
│           └─ core.py
├─ backend/            # FastAPI HTTP API
│   ├─ pyproject.toml
│   └─ app/
│       ├─ __init__.py
│       └─ main.py
├─ frontend/           # Vite + React + TypeScript UI
│   ├─ package.json
│   ├─ vite.config.ts
│   └─ src/
│       └─ main.tsx
├─ tests/              # pytest suite
│   ├─ pytest.ini
│   └─ test_sdk.py
├─ docs/               # documentation and learning notes
│   ├─ architecture.md
│   ├─ privacy.md
│   └─ learning-notes.md
├─ .gitignore
├─ README.md           # (this file)
└─ .env.example
```

## Setup

### Python side
```bash
# create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate

# install the SDK in editable mode (includes dev deps)
pip install -e ./sdk[dev]
```

### Node / frontend side
```bash
cd frontend
npm install   # installs Vite, React, TypeScript
npm run dev    # starts the dev server on http://localhost:5173
```

The frontend will query the FastAPI health endpoint (`http://127.0.0.1:8000/health`).

### Backend
```bash
pip install -e ./backend   # installs FastAPI & Uvicorn
uvicorn backend.app.main:app --reload
```

## Roadmap (high‑level)
1. **Phase 1** – scaffolding (this repository).
2. **Phase 2** – core engine: tokenisation with *tiktoken*, classification, report model.
3. **Phase 3** – persistence (SQLite) and richer API endpoints.
4. **Phase 4** – full dashboard with D3 minimap, optimisation suggestions.

---

*All code in this phase is intentionally minimal and does **not** perform any real token analysis yet.*
