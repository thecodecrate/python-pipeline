from typing import Any, Protocol, TypeVar


class PipelineInterface(
    Protocol,
):
    def __init__(self, *args: Any, **kwds: Any) -> None: ...


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
