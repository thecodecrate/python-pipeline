from typing import Any, Self, Optional

from ..with_pipeline_processor.processor_interface import ProcessorInterface
from ..with_base.type_pipeline_callable import PipelineCallable
from ..with_base.type_payload import TPayload
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
):
    def __init__(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self.set_items(self.get_items() or []).set_processor(
            processor or self.get_processor()
        )

    def pipe(self, stage: PipelineCallable[TPayload, ...]) -> Self:
        return self.add_item(stage)
