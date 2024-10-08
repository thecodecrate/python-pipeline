from typing import Optional, Protocol, Self

from ..with_base.types import T_in, T_out
from .pipelineable_facade import PipelineableFacade
from ..with_base.stage_callable import StageCallableType
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_pipeline_processor.processor_interface import ProcessorInterface


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    def build(
        self,
        processor: Optional[ProcessorInterface[T_in, T_out]] = None,
    ) -> PipelineableFacade[T_in, T_out]: ...

    def add(self, item: StageCallableType) -> Self: ...
