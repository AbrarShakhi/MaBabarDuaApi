from typing import Callable, Optional

from .exceptions import HTTPException


class MaBabarDuaApi:
    def __init__(self, middlewares: Optional[list[Callable]] = None) -> None:
        self.router = None
        self._global_middlewares: list[Callable] = middlewares or []

    