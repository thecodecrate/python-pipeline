from typing import Any, Optional, Self

from ...support.act_as_factory import ActAsFactory
from ...support.act_as_list import ActAsList
from ..step01_base import (
    StageClassOrInstance,
    StageCollection,
    TPipeline,
)
from .pipeline_factory_interface import PipelineFactoryInterface as ImplementsInterface


class PipelineFactory(
    ActAsFactory[TPipeline],
    ActAsList[StageClassOrInstance, StageCollection],
    ImplementsInterface[TPipeline],
):
    _model_class: Optional[type[TPipeline]]  # ActAsFactory
    stages: StageCollection  # ActAsList

    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        model_class: Optional[type[TPipeline]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "_model_class"):
            self._model_class = None

        if stages:
            self.stages = stages

        if model_class:
            self._model_class = model_class

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
        """
        Adds a single stage to the pipeline.
        """
        return self._add_item(stage)

    # public API: factory configuration
    def with_stages(self, stages: StageCollection) -> Self:
        """
        Adds a collection of stages to the pipeline.
        """
        return self._set_items(stages)
