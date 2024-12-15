from typing import Any, Generic, Optional, Self

from ...support.act_as_factory import ActAsFactory
from ...support.act_as_list import ActAsList
from ..step01_base.pipeline_interface import TPipeline
from ..step01_base.stage_callable import (
    StageClassOrInstance,
    StageCollection,
)
from .pipeline_factory_interface import PipelineFactoryInterface


class PipelineFactory(
    PipelineFactoryInterface[TPipeline],
    ActAsFactory[TPipeline],
    ActAsList[StageClassOrInstance, StageCollection],
    Generic[TPipeline],
):
    _model_class: Optional[type[TPipeline]]  # ActAsFactory
    stages: StageCollection  # ActAsList

    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "_model_class"):
            self._model_class = None

        if stages:
            self.stages = stages

    # ActAsList
    def _get_items(self) -> StageCollection:
        return self.stages

    # ActAsList
    def _set_items(self, items: StageCollection) -> Self:
        self.stages = items

        return self

    # ActAsList
    def _add_item(self, item: StageClassOrInstance) -> Self:
        return self._set_items(self.stages + (item,))

    # ActAsFactory
    def _definition(self) -> dict[str, Any]:
        return {"stages": self._get_items()}

    # public API: factory configuration
    def add_stage(self, stage: StageClassOrInstance) -> Self:
        return self._add_item(stage)

    # public API: factory configuration
    def with_stages(self, stages: StageCollection) -> Self:
        return self._set_items(stages)
