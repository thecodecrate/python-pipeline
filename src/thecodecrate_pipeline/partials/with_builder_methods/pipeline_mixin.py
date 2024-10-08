from abc import ABC
from typing import Any, Generic, Optional, Self

from ..with_base.types import T_in, T_out
from .pipelineable_facade import TPipelineable
from ..with_base.stage_callable import StageCallableType
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_pipeline_processor.processor_interface import ProcessorInterface


class PipelineMixin(
    ImplementsPipelineInterface[T_in, T_out],
    Generic[TPipelineable, T_in, T_out],
    ABC,
):
    pipelineable_class: type[TPipelineable]

    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self.set_items(self.get_items() or [])

    def add(self, item: StageCallableType) -> Self:
        return self.add_item(item)

    def build(
        self,
        processor: Optional[ProcessorInterface[T_in, T_out]] = None,
    ) -> TPipelineable:
        pipelineable = self.pipelineable_class()

        return pipelineable.set_items(
            [*self.get_items()],
        ).set_processor(
            processor or pipelineable.get_processor(),
        )
