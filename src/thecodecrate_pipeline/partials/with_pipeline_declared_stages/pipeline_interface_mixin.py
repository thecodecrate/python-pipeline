from typing import Any, Protocol, Self

from .stage_facade import StageFacade
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_base.stage_callable import StageCallableType
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)

StageClassOrInstance = type[StageFacade[Any, Any]] | StageCallableType


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol,
):
    def _should_instantiate_stages(self) -> bool: ...

    def _instantiate_stages(self) -> Self: ...

    def with_stages(self, stages: list[StageClassOrInstance]) -> Self: ...
