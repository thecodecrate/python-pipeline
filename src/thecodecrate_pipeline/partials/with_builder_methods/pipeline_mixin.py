from abc import ABC
from typing import Generic, Optional, Self

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

    def add(self, item: StageCallableType) -> Self:
        return self.add_item(item)

    def build(
        self,
        processor: Optional[ProcessorInterface[T_in, T_out]] = None,
    ) -> TPipelineable:
        return self.pipelineable_class(
            stage_instances=self.get_items(),
            processor=processor,
        )
