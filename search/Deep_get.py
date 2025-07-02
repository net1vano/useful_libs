from typing import Any, List


def deep_get(data: dict | list, *keys, default=None) -> Any:
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return default
    return current

data = {
    "user": {
        "address": {
            "city": "Moscow",
            "zip": "12345"
        }
    },
    "roles": ["admin", "moderator"]
}

value = deep_get(data, "user", "address", "city")
print(value)