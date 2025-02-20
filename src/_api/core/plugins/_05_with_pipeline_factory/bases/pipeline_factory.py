from typing import Any, Optional, Self

# extends: 3rd-party concrete
from ....support.act_as_factory import ActAsFactory
from ....support.act_as_list import ActAsList
from ..bridges.pipeline_interface import TPipeline

# uses: bridge interfaces
from ..bridges.stage_callable import StageClassOrInstance, StageCollection

# implements: self-interface
from .pipeline_factory_interface import PipelineFactoryInterface as ImplementsInterface


class PipelineFactory(
    ActAsFactory[TPipeline],
    ActAsList[StageClassOrInstance, StageCollection],
    ImplementsInterface[TPipeline],
):
    stages: StageCollection  # ActAsList
    pipeline_class: Optional[type[TPipeline]]

    def __init__(
        self,
        stages: Optional[StageCollection] = None,
        pipeline_class: Optional[type[TPipeline]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "pipeline_class"):
            self.pipeline_class = self._get_default_pipeline_class()

        if stages:
            self.stages = stages

        if pipeline_class:
            self.pipeline_class = pipeline_class

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
    def _get_model_class(self) -> type[TPipeline]:
        if self.pipeline_class is None:
            raise ValueError("Pipeline class not set in factory.")

        return self.pipeline_class

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

    def _get_default_pipeline_class(self) -> Optional[type[TPipeline]]:
        return None
