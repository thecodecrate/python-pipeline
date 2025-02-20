from typing import Any, Optional, Protocol, Self

# extends: self-bridge
from ..bridges.pipeline_interface import PipelineInterface

# uses: bridge interface
from ..bridges.stage_callable import StageCollection


class PipelineInterfaceMixin(
    PipelineInterface,
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
