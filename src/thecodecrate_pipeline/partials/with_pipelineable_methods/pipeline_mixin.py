from typing import Any, Self, Optional

from ..with_pipeline_processor.processor_interface import ProcessorInterface
from ..with_base.stage_callable import StageCallable
from ..with_base.payload_type import TPayload
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

    def pipe(self, stage: StageCallable[TPayload]) -> Self:
        return self.add_item(stage)
