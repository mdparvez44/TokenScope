# Privacy policy for TokenScope (Phase 1)

**Local‑first processing** – All analysis of LLM context is performed on the developer's machine. No network requests are made, and no telemetry, analytics, or usage data leave the host.

**Data handling**
- The tool reads only the files or strings explicitly passed to the SDK (`analyze_context`).
- No temporary files are written outside the project's directory except for optional SQLite databases (future phase).
- Environment variables (e.g., API keys) are never accessed; the `.env.example` provides placeholders for local configuration only.

**Security considerations**
- The repository includes a `.gitignore` that excludes `.env` files and any generated SQLite databases.
- All third‑party dependencies are pinned to known versions and are open‑source.

**Future phases** – Should external services be integrated (e.g., remote LLM APIs), a clear opt‑in consent flow will be added, and the privacy policy will be updated accordingly.
