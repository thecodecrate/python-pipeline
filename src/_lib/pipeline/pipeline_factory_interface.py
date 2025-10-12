from typing import Any, Optional, Protocol, Self

from .callable_type import StageDefinition, StageDefinitionCollection
from .pipeline_interface import PipelineInterface
from .traits.act_as_factory.act_as_factory_interface import ActAsFactoryInterface
from .types import T_in, T_out


class PipelineFactoryInterface(
    ActAsFactoryInterface[PipelineInterface[T_in, T_out]],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        pipeline_class: Optional[type[PipelineInterface[T_in, T_out]]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageDefinition) -> Self: ...

    def with_stages(self, stages: StageDefinitionCollection) -> Self: ...
