from typing import Any, Protocol


class PipelineInterface(
    Protocol,
):
    def __init__(self, *args: Any, **kwds: Any) -> None: ...
