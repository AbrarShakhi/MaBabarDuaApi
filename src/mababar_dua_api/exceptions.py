class HTTPException(Exception):
    def __init__(self, status_code: int, detail: str = "") -> None:
        self.status_code = status_code
        self.detail = detail or self._default_detail(status_code)
        super().__init__(self.detail)

    @staticmethod
    def _default_detail(status_code: int) -> str:
        defaults = {}
        return defaults.get(status_code, "HTTP Error")
