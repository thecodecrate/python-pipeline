from typing import Any, Optional, Protocol, Self

# extends: 3rd-party interface
from ....support.act_as_factory import ActAsFactoryInterface
from ....support.act_as_list import ActAsListInterface

# uses: bridge interface
from ..bridges.pipeline_interface import TPipeline
from ..bridges.stage_callable import StageClassOrInstance, StageCollection


class PipelineFactoryInterface(
    ActAsFactoryInterface[TPipeline],
    ActAsListInterface[StageClassOrInstance, StageCollection],
    Protocol[TPipeline],
):
    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        pipeline_class: Optional[type[TPipeline]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def add_stage(self, stage: StageClassOrInstance) -> Self: ...

    def with_stages(self, stages: StageCollection) -> Self: ...

    def _get_default_pipeline_class(self) -> Optional[type[TPipeline]]: ...
