from typing import Any, Generic, Optional, Self

from .pipeline_factory_interface import PipelineFactoryInterface
from ..with_base.pipeline_interface import TPipeline
from ..with_pipeline_declared_stages.pipeline_mixin import StageClassOrInstance
from ...support.act_as_factory import ActAsFactory
from ...support.act_as_list import ActAsList


class PipelineFactory(
    PipelineFactoryInterface[TPipeline],
    ActAsFactory[TPipeline],
    ActAsList[StageClassOrInstance],
    Generic[TPipeline],
):
    _instance_class: Optional[type[TPipeline]] = None  # ActAsFactory
    stages: list[StageClassOrInstance] = []  # ActAsList

    def __init__(
        self,
        stages: list[StageClassOrInstance] = [],
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not self.stages:
            self.stages = [*stages] or []

    # ActAsList
    def _get_items(self) -> list[StageClassOrInstance]:
        return self.stages

    # ActAsList
    def _set_items(self, items: list[StageClassOrInstance]) -> Self:
        self.stages = items

        return self

    # ActAsFactory
    def _definition(self) -> dict[str, Any]:
        return {"stages": self._get_items()}

    # User factory configuration
    def add_stage(self, stage: StageClassOrInstance) -> Self:
        return self._add_item(stage)

    # User factory configuration
    def with_stages(self, stages: list[StageClassOrInstance]) -> Self:
        return self._set_items([*stages])
