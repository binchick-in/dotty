from __future__ import annotations

import json
from typing import Any


class Dotty:
    def __init__(self, data: dict[Any, Any]):
        self._data = data

    def __getattr__(self, key: Any) -> Any:
        if not self._data.get(key):
            raise KeyError(f"{key} not found in root data")

        if isinstance(self._data[key], dict):
            return Dotty(self._data[key])

        return self._data.get(key)

    def json(self) -> str:
        return json.dumps(self._data)
