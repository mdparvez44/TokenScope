import pytest
from tokenscope import analyze_context, ContextReport


def test_import_and_placeholder():
    # Simple import check already done, now test placeholder function returns a ContextReport
    messages = [{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}]
    report = analyze_context(messages)
    assert isinstance(report, ContextReport)
    assert len(report.segments) == 2
    assert report.segments[0].category == "system"
    assert report.segments[1].category == "user"
