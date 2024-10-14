from typing import Any, Optional, Protocol, Self

from ..with_base.pipeline_interface import TPipeline
from ..with_pipeline_declared_stages.pipeline_mixin import StageClassOrInstance
from ...support.act_as_factory import ActAsFactoryInterface
from ...support.act_as_list import ActAsListInterface


class PipelineFactoryInterface(
    ActAsFactoryInterface[TPipeline],
    ActAsListInterface[StageClassOrInstance],
    Protocol[TPipeline],
):
    def __init__(
        self,
        stages: Optional[list[StageClassOrInstance]] = [],
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageClassOrInstance) -> Self: ...

    def with_stages(self, stages: list[StageClassOrInstance]) -> Self: ...
