# Architecture Overview (Phase 1)

TokenScope is organised into five bounded contexts to keep concerns separated and enable independent evolution.

| Context | Responsibility | Language / Tech |
|---|---|---|
| **SDK** | Public Python API (`tokenscope` package). Pure‑Python, no web or UI dependencies. Provides `analyze_context` and data models. | Python, Pydantic |
| **Core engine** | Analysis logic (tokenisation, classification, risk heuristics). Lives in `tokenscope.core`. | Python |
| **Backend** | Local HTTP API exposing SDK functionality. Implemented with **FastAPI**. | Python, FastAPI |
| **Frontend** | Interactive dashboard built with **React**, **TypeScript**, **Vite**. Talks to backend over HTTP. | TypeScript, React, Vite |
| **CLI** | Convenience commands for running analysis locally and launching the dashboard (to be added later). | Python (click/typer) |

### Rationale
* **Separation of concerns** – the core engine can be unit‑tested without a server.
* **Language boundaries** – Python excels at data processing, while React/TS provides a responsive UI.
* **Future‑proof** – the SDK can be published independently; the backend can be used by other services; the frontend can be swapped without touching the core.

### Alternatives considered
* Monolithic repo mixing FastAPI and React code – rejected because it blurs responsibilities and hurts testability.
* Rust for the engine – rejected for the current team’s Python expertise and the low performance need in Phase 1.
* Next.js instead of Vite – rejected due to unnecessary SSR complexity for a pure client‑side dashboard.

---

*This document will be expanded as the project evolves.*
