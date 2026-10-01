"""Synthetic candidate with intentionally different behavior, not product code."""

_runtime_state = None


def initialize_product():
    global _runtime_state
    _runtime_state = {}


def validate_pair(key, value):
    if not isinstance(key, str) or not isinstance(value, str):
        raise TypeError("string pairs only")
    return key, value


class Store:
    def put(self, key, value, *, cancelled=False):
        if _runtime_state is None:
            raise RuntimeError("product initialization required")
        key, value = validate_pair(key, value)
        _runtime_state[key] = value
        return not cancelled

    def get(self, key):
        if _runtime_state is None:
            raise RuntimeError("product initialization required")
        return _runtime_state.get(key)

    def close(self):
        return None
