from typing import Optional, Protocol, Self

from .pipelineable_facade import TPipelineable
from ..with_base.type_pipeline_callable import PipelineCallable
from ..with_base.type_payload import TPayload
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_pipeline_processor.processor_interface import ProcessorInterface


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
    Protocol[TPayload, TPipelineable],
):
    pipelineable_class: type[TPipelineable]

    def __init__(self) -> None:
        super().__init__()

        self.set_items(self.get_items() or [])

    def add(self, item: PipelineCallable[TPayload, ...]) -> Self:
        return self.add_item(item)

    def build(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> TPipelineable:
        pipelineable = self.pipelineable_class()

        return pipelineable.set_items(
            [*self.get_items()],
        ).set_processor(
            processor or pipelineable.get_processor(),
        )
