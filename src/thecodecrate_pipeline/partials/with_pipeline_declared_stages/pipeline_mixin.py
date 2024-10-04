from typing import Any, Generic

from thecodecrate_pipeline.partials.with_base.type_pipeline_callable import (
    PipelineCallable,
)

from .stage_facade import StageFacade
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.type_payload import TPayload

PipelineCallableOrStage = (
    type[StageFacade[TPayload]]
    | StageFacade[TPayload]
    | PipelineCallable[TPayload, ...]
)


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
    Generic[TPayload],
):
    stages: list[PipelineCallableOrStage[TPayload]] = []

    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)

        self._instantiate_stages()

    def _instantiate_stages(self) -> None:
        self.stage_instances = [
            stage() if isinstance(stage, type) else stage
            for stage in self.stages
        ]
