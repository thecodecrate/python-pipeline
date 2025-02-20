from typing import Any

# extends: 3rd-party concrete
from ....support.clonable import Clonable

# implements: self-interface
from .pipeline_interface import PipelineInterface as ImplementsInterface


class Pipeline(
    Clonable,
    ImplementsInterface,
):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        pass
