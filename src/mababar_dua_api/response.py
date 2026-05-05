import json
import re
from typing import Any, Callable, Optional


class Response:
    media_type = "text/plain"

    def __init__(
        self,
        content: str = "",
        status_code: int = 200,
        headers: Optional[dict] = None,
    ) -> None:
        self._content = content
        self._status_code = status_code
        self._extra_headers: dict[str, str] = headers or {}


class JSONResponse(Response):
    media_type = "application/json"

    def __init__(
        self,
        content: Any = None,
        status_code: int = 200,
        headers: Optional[dict] = None,
    ) -> None:
        super().__init__(
            content=json.dumps(content),
            status_code=status_code,
            headers=headers,
        )


class HTMLResponse(Response):
    media_type = "text/html"
