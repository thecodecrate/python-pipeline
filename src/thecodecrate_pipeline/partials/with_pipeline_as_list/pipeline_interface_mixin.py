from typing import Any, Optional, Protocol, Self

from ..with_base.stage_callable import StageCallableType
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ...support.act_as_list.act_as_list_interface import (
    ActAsListInterface,
)


class PipelineInterfaceMixin(
    ActAsListInterface[StageCallableType],
    WithPipelineBaseInterface,
    Protocol,
):
    def __init__(
        self,
        stage_instances: Optional[list[StageCallableType]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def pipe(self, stage: StageCallableType) -> Self: ...
