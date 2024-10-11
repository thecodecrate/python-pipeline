from typing import Any

from .stage_facade import StageFacade
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.stage_callable import StageCallableType

StageClassOrInstance = type[StageFacade[Any, Any]] | StageCallableType


class PipelineMixin(
    ImplementsPipelineInterface,
):
    stages: list[StageClassOrInstance] = []

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if self._should_instantiate_stages():
            self._instantiate_stages()

    def _should_instantiate_stages(self) -> bool:
        return len(self.get_items()) == 0 and len(self.stages) > 0

    def _instantiate_stages(self) -> None:
        instances = [
            stage() if isinstance(stage, type) else stage
            for stage in self.stages
        ]

        self.set_items(instances)
