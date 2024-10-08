from typing import Any, Generic, Optional, Self

from .pipelineable_facade import TPipelineable
from ..with_base.stage_callable import StageCallable
from ..with_base.payload_type import TPayload
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_pipeline_processor.processor_interface import ProcessorInterface


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
    Generic[TPayload, TPipelineable],
):
    pipelineable_class: type[TPipelineable]

    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self.set_items(self.get_items() or [])

    def add(self, item: StageCallable[TPayload]) -> Self:
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
