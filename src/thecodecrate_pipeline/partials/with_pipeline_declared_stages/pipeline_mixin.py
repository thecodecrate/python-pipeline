from typing import Any, Optional, Self

from ..with_base.stage_callable import StageCollection
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)


class PipelineMixin(
    ImplementsPipelineInterface,
):
    stages: StageCollection

    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "stages"):
            self.stages = tuple()

        if stages:
            self.stages = stages

        if self._should_instantiate_stages():
            self._instantiate_stages()

    def _should_instantiate_stages(self) -> bool:
        return len(self._get_items()) == 0 and len(self.stages) > 0

    def _instantiate_stages(self) -> Self:
        instances = tuple(
            stage() if isinstance(stage, type) else stage
            for stage in self.stages
        )

        return self._set_items(instances)

    def with_stages(self, stages: StageCollection) -> Self:
        cloned = self.clone({"stages": stages, "stage_instances": []})

        return cloned._instantiate_stages()
