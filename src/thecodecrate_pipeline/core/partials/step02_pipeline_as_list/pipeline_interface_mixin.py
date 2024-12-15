from typing import Any, Optional, Protocol, Self

from ...support.act_as_list.act_as_list_interface import (
    ActAsListInterface,
)
from ..step01_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..step01_base.stage_callable import StageInstance, StageInstanceCollection


class PipelineInterfaceMixin(
    ActAsListInterface[StageInstance, StageInstanceCollection],
    WithPipelineBaseInterface,
    Protocol,
):
    def __init__(
        self,
        stage_instances: Optional[StageInstanceCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def pipe(self, stage: StageInstance) -> Self: ...
