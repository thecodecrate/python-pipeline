from typing import Any, Optional, Protocol, Self

from ..types.callable_type import (
    CallableCollection,
    CallableType,
    StageDefinitionCollection,
)
from ..types.types import T_in, T_out
from .base_pipeline import BasePipeline as BasePipelineContract


class StageablePipeline(
    BasePipelineContract[T_in, T_out],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        stages_instances: Optional[CallableCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def pipe(self, stage: CallableType) -> Self: ...

    def with_stages(self, stages: StageDefinitionCollection) -> Self: ...

    def get_stages(self) -> StageDefinitionCollection: ...

    def get_stages_instances(self) -> CallableCollection: ...
