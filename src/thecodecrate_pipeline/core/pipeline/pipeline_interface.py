from typing import Generic, Optional, Protocol
from ...traits.with_stages.with_stages import WithStages
from ...traits.with_builderable.with_builderable import WithBuilderable
from ...traits.with_callable_pipeline.with_callable_pipeline import (
    WithCallablePipeline,
)
from ...traits.with_pipe.with_pipe import WithPipe
from ...traits.with_processor.processor_interface import ProcessorInterface
from ...traits.with_processor.with_processor import WithProcessor
from ...traits.with_immutability.with_immutability import WithImmutability
from .pipeline_callable import PipelineCallable
from .payload import TPayload


class PipelineInterface(
    WithImmutability[TPayload],
    WithCallablePipeline[TPayload],
    WithProcessor[TPayload],
    WithPipe[TPayload],
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
        stages: Optional[list[PipelineCallable[TPayload]]] = None,
    ) -> None:
        self.set_processor(processor or self.get_processor())

        self.set_parts([*stages] if stages else self.get_parts())
