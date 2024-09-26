from typing import Generic

from ..pipeline.payload import TPayload
from .pipeline_builder_interface import PipelineBuilderInterface


class PipelineBuilder(
    PipelineBuilderInterface[TPayload],
    Generic[TPayload],
):
    def __init__(self) -> None:
        self.stages = []
