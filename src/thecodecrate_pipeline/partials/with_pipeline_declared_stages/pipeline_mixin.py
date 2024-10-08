from typing import Any

from ..with_base.stage_callable import StageCallable
from .stage_facade import StageFacade
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.payload_type import TPayload

StageClassOrInstance = type[StageFacade[TPayload]] | StageCallable[TPayload]


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
):
    stages: list[StageClassOrInstance[TPayload]] = []

    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self._instantiate_stages()

    def _instantiate_stages(self) -> None:
        instances = [
            stage() if isinstance(stage, type) else stage
            for stage in self.stages
        ]

        self.set_items(instances)
