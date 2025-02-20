from typing import Any, Protocol, TypeVar

# extend: 3rd-party interface
from ....support.clonable import ClonableInterface


class PipelineInterface(
    ClonableInterface,
    Protocol,
):
    def __init__(self, *args: Any, **kwds: Any) -> None: ...


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
