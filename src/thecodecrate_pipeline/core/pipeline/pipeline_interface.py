from abc import ABC, abstractmethod
from typing import Generic, Optional

from ...support.libraries.builderable import Builderable
from ...traits.with_stages.with_stages import WithStages
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
    WithImmutability["PipelineInterface[TPayload]", TPayload],
    WithCallablePipeline["PipelineInterface[TPayload]", TPayload],
    WithProcessor["PipelineInterface[TPayload]", TPayload],
    WithPipe["PipelineInterface[TPayload]", TPayload],
    WithStages["PipelineInterface[TPayload]", TPayload],
    Builderable[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    @abstractmethod
    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
        stages: Optional[list[PipelineCallable[TPayload]]] = None,
    ) -> None:
        pass
