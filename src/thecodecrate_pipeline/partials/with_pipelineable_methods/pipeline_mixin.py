from typing import Protocol, Self, Optional

from ..with_pipeline_processor.processor_interface import ProcessorInterface
from ..with_base.type_pipeline_item import PipelineItem
from ..with_base.type_payload import TPayload
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)


class PipelineMixin(
    PipelineInterface[TPayload],
    Protocol[TPayload],
):
    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> None:
        super().__init__()

        self.set_items(self.get_items() or []).set_processor(
            processor or self.get_processor()
        )

    def pipe(self, stage: PipelineItem[TPayload, ...]) -> Self:
        return self.add_item(stage)
