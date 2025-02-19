from typing import Any, Optional, Protocol, Self

from ...support.act_as_factory import ActAsFactoryInterface
from ...support.act_as_list import ActAsListInterface
from ..step01_base import StageClassOrInstance, StageCollection, TPipeline


class PipelineFactoryInterface(
    ActAsFactoryInterface[TPipeline],
    ActAsListInterface[StageClassOrInstance, StageCollection],
    Protocol[TPipeline],
):
    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        model_class: Optional[type[TPipeline]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageClassOrInstance) -> Self: ...

    def with_stages(self, stages: StageCollection) -> Self: ...
