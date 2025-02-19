from typing import Any, Optional, Protocol, Self

from ..step01_base import (
    Pipeline_Base_Interface,
    StageCollection,
)
from ..step02_pipeline_as_list import (
    Pipeline_WithPipelineAsList_Interface,
)


class PipelineInterfaceMixin(
    Pipeline_WithPipelineAsList_Interface,
    Pipeline_Base_Interface,
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
