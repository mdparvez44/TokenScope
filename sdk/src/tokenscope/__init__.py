"""tokenscope SDK package.

Provides the public developer‑facing API for analyzing LLM context.

Only the minimal stub is provided in Phase 1; the core engine lives in
`tokenscope.core` and will be expanded later.
"""

from .core import ContextReport, analyze_context  # noqa: F401
