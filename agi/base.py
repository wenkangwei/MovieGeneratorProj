import abc
from typing import Any

class BaseAGI(abc.ABC):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
    def query(self, text: str, mode: str) -> Any:
        return super().query(text, mode)