"""Synthetic target contract; do not import/run during a static-only review."""

def exercise_required_behavior(factory):
    first, second = factory(), factory()
    first.put("key", "first")
    assert second.get("key") is None
    assert first.put("cancelled", "value", cancelled=True) is False
    assert first.get("cancelled") is None
    first.close()
    try:
        first.put("late", "value")
    except RuntimeError:
        pass
    else:
        raise AssertionError("closed instances must refuse writes")
