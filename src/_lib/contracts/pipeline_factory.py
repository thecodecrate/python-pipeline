from typing import Any, Optional, Protocol, Self

from ..support.act_as_factory.act_as_factory_interface import ActAsFactoryInterface
from ..types.callable_type import StageDefinition, StageDefinitionCollection
from ..types.types import T_in, T_out
from .pipeline import Pipeline as PipelineContract


class PipelineFactory(
    ActAsFactoryInterface[PipelineContract[T_in, T_out]],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        pipeline_class: Optional[type[PipelineContract[T_in, T_out]]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageDefinition) -> Self: ...

    def with_stages(self, stages: StageDefinitionCollection) -> Self: ...
