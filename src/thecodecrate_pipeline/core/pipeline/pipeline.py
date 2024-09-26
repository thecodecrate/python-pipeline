from typing import Generic, Optional

from .pipeline_callable import PipelineCallable
from .payload import TPayload
from .pipeline_interface import PipelineInterface
from ...modules.processors.chained_processor import ChainedProcessor
from ...traits.with_processor.processor_interface import ProcessorInterface


class Pipeline(
    PipelineInterface[TPayload],
    Generic[TPayload],
):
    processor_class = ChainedProcessor

    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
        stages: Optional[list[PipelineCallable[TPayload]]] = None,
    ) -> None:
        self.processor = processor or self.get_processor()

        self.stages = [*stages] if stages else []
