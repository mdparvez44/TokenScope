"""Core engine stub for TokenScope.

The core engine is deliberately lightweight in Phase 1 – it only defines the
public data model `ContextReport` and a placeholder function
`analyze_context` that will be implemented later.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field


class ContextSegment(BaseModel):
    """A single segment of the LLM request.

    In later phases this will include token counts, category, start/end
    positions, etc. For now it is only a placeholder to illustrate the shape
    of the eventual report.
    """

    index: int = Field(..., description="Zero‑based segment index")
    category: str = Field(..., description="One of the context categories")
    content: str = Field(..., description="Raw text of the segment")


class ContextReport(BaseModel):
    """Top‑level report model produced by the SDK.

    The report is the contract between the SDK, the FastAPI backend, and the
    frontend. It will grow to contain token statistics, risk warnings, and
    optimisation recommendations.
    """

    total_tokens: int = Field(0, description="Total token count (placeholder)")
    segments: List[ContextSegment] = Field(default_factory=list, description="List of analysed segments")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional information, version, timestamps, etc.")


def analyze_context(messages: List[Dict[str, Any]]) -> ContextReport:
    """Placeholder analysis function.

    Parameters
    ----------
    messages: List[Dict[str, Any]]
        The raw LLM messages as a list of dictionaries. Each dict should have a
        ``role`` (e.g., ``"system"``, ``"user"``) and ``content`` field.

    Returns
    -------
    ContextReport
        A minimal report containing the raw messages as ``ContextSegment``
        objects. Real tokenisation and classification will be added later.
    """

    segments = [
        ContextSegment(index=i, category=msg.get("role", "unknown"), content=msg.get("content", ""))
        for i, msg in enumerate(messages)
    ]
    return ContextReport(total_tokens=0, segments=segments, metadata={"placeholder": True})
