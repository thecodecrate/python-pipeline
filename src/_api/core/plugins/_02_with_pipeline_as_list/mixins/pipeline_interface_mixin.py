from typing import Any, Optional, Protocol, Self

# extends: 3rd-party interface
from ....support.act_as_list import ActAsListInterface

# extends: self-bridge
from ..bridges.pipeline_interface import PipelineInterface

# uses: bridge interface
from ..bridges.stage_callable import (
    StageInstance,
    StageInstanceCollection,
)


class PipelineInterfaceMixin(
    ActAsListInterface[StageInstance, StageInstanceCollection],
    PipelineInterface,
    Protocol,
):
    def __init__(
        self,
        stage_instances: Optional[StageInstanceCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def pipe(self, stage: StageInstance) -> Self: ...
