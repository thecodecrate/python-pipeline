from abc import ABC
from typing import Any, Self, Optional

from ..with_base.types import T_in, T_out
from ..with_pipeline_processor.processor_interface import ProcessorInterface
from ..with_base.stage_callable import StageCallableType
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)


class PipelineMixin(
    ImplementsPipelineInterface[T_in, T_out],
    ABC,
):
    def __init__(
        self,
        processor: Optional[ProcessorInterface[T_in, T_out]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self.set_items(self.get_items() or []).set_processor(
            processor or self.get_processor()
        )

    def pipe(self, stage: StageCallableType) -> Self:
        return self.add_item(stage)
