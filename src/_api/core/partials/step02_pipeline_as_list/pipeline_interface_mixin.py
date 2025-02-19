from typing import Any, Optional, Protocol, Self

from ...support.act_as_list.act_as_list_interface import (
    ActAsListInterface,
)
from ..step01_base import (
    Pipeline_Base_Interface,
    StageInstance,
    StageInstanceCollection,
)


class PipelineInterfaceMixin(
    ActAsListInterface[StageInstance, StageInstanceCollection],
    Pipeline_Base_Interface,
    Protocol,
):
    def __init__(
        self,
        stage_instances: Optional[StageInstanceCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def pipe(self, stage: StageInstance) -> Self: ...
