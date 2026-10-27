```markdown
# Architecture Overview (Phase 1)

TokenScope is organised into **five bounded contexts** that keep concerns separate and make the codebase easy to evolve.

| Context | Responsibility | Typical language / technology |
|---------|----------------|-------------------------------|
| **SDK** | Public Python API (`tokenscope` package). Pure‑Python, no web framework or UI dependencies. Provides `analyze_context` and data models that will be shared with the backend and frontend. | Python, Pydantic |
| **Core engine** | The actual analysis logic (tokenisation, segment classification, risk heuristics). Lives inside `tokenscope.core` and is imported by the SDK. | Python |
| **Backend** | Local HTTP API exposing the SDK functionality. Implemented with **FastAPI**; runs on `127.0.0.1:8000` in development. | Python, FastAPI |
| **Frontend** | Interactive dashboard built with **React**, **TypeScript**, and **Vite**. It talks to the backend over HTTP and visualises the `ContextReport`. | TypeScript, React, Vite, D3 (later) |
| **CLI** | Convenience commands (`tokenscope-cli`) to run analysis locally and start the dashboard. Will be added later (outside Phase 1). | Python (click/typer) |

### Why this layout?
* **Separation of concerns** – the core engine can be unit‑tested without spinning up a web server.
* **Language boundaries** – Python for the heavy lifting, JavaScript/TypeScript for the UI, keeping each ecosystem happy.
* **Future‑proof** – the SDK can be published to PyPI later; the backend can be used by other services; the frontend can be swapped for a different UI framework without touching the core.

### Alternatives considered
* **Monolithic single package** – would intertwine FastAPI and React code, making testing and reuse harder.
* **Rust for the engine** – rejected because the team prefers Python for rapid iteration and the project’s initial scope does not need the performance gains of Rust.
* **Next.js instead of Vite** – Next.js adds SSR complexity we don’t need yet; Vite is lightweight for a pure‑client dashboard.

### Trade‑offs
* Slightly more scaffolding upfront, but the payoff is clearer module boundaries.
* Two `pyproject.toml` files (SDK and backend) add a tiny maintenance burden; we could merge them later after the SDK stabilises.

---

**Learning notes** – this file is intentionally verbose to teach the developer about each component, the choices made, and how they interact. Feel free to ask for deeper explanations on any part.
```
