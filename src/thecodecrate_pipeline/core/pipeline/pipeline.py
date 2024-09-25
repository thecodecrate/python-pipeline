from typing import Generic, Optional
from ...modules.processors.chained_processor import ChainedProcessor
from ...traits.with_processor.processor_interface import ProcessorInterface
from .payload import TPayload
from .pipeline_interface import PipelineInterface


class Pipeline(
    PipelineInterface[TPayload],
    Generic[TPayload],
):
    processor_class = ChainedProcessor

    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> None:
        self.parts = []

        self.processor = processor or self.get_processor()
