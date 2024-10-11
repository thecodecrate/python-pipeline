from typing import Any
from .pipeline_interface import (
    PipelineInterface as ImplementsPipelineInterface,
)


class Pipeline(
    ImplementsPipelineInterface,
):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        pass
