from typing import Any

from ...support.clonable import Clonable
from .pipeline_interface import (
    PipelineInterface as ImplementsInterface,
)


class Pipeline(
    Clonable,
    ImplementsInterface,
):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        pass
