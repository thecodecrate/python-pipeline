from typing import Protocol, Self

from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)


class PipelineInterfaceMixin(
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    def pipe(self, stage: StageCallableType) -> Self: ...
