from abc import ABC
from typing import Any, Optional, Self

from ..contracts.stageable_pipeline import StageablePipeline as ImplementsInterface
from ..types.callable_type import (
    CallableCollection,
    CallableType,
    StageDefinitionCollection,
)
from ..types.types import T_in, T_out


class StageablePipeline(
    ImplementsInterface[T_in, T_out],
    ABC,
):
    stages: StageDefinitionCollection
    stages_instances: CallableCollection

    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        stages_instances: Optional[CallableCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "stages_instances"):
            self.stages_instances = tuple()

        if stages:
            self.stages = stages

        if stages_instances:
            self.stages_instances = stages_instances

        if self._should_instantiate_stages():
            self._instantiate_stages()

    def pipe(self, stage: CallableType) -> Self:
        """
        Adds a single stage to the pipeline.
        """
        return self.clone({"stages_instances": tuple([*self.stages_instances, stage])})

    def with_stages(self, stages: StageDefinitionCollection) -> Self:
        """
        Adds a collection of stages to the pipeline.
        """
        cloned = self.clone({"stages": stages, "stages_instances": []})

        return cloned._instantiate_stages()

    def get_stages(self) -> StageDefinitionCollection:
        return self.stages

    def get_stages_instances(self) -> CallableCollection:
        return self.stages_instances

    def _should_instantiate_stages(self) -> bool:
        return len(self.stages_instances) == 0 and len(self.stages) > 0

    def _instantiate_stages(self) -> Self:
        self.stages_instances = tuple(
            stage() if isinstance(stage, type) else stage for stage in self.stages
        )

        return self
