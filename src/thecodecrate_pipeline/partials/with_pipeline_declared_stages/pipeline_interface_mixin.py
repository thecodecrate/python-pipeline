from typing import Any, Optional, Protocol, Self

from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_base.stage_callable import StageCollection
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol,
):
    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def _should_instantiate_stages(self) -> bool: ...

    def _instantiate_stages(self) -> Self: ...

    def with_stages(self, stages: StageCollection) -> Self: ...
