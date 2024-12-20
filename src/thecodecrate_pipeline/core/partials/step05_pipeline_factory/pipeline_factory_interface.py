from typing import Any, Optional, Protocol, Self

from ...support.act_as_factory import ActAsFactoryInterface
from ...support.act_as_list import ActAsListInterface
from ..step01_base.pipeline_interface import TPipeline
from ..step01_base.stage_callable import StageClassOrInstance, StageCollection


class PipelineFactoryInterface(
    ActAsFactoryInterface[TPipeline],
    ActAsListInterface[StageClassOrInstance, StageCollection],
    Protocol[TPipeline],
):
    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageClassOrInstance) -> Self: ...

    def with_stages(self, stages: StageCollection) -> Self: ...
