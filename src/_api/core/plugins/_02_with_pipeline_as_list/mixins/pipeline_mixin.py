from abc import ABC
from typing import Any, Optional, Self

# extends: 3rd-party concrete
from ....support.act_as_list import ActAsList

# uses: bridge interfaces
from ..bridges.stage_callable import StageInstance, StageInstanceCollection

# implements: self-interface
from .pipeline_interface_mixin import PipelineInterfaceMixin as ImplementsInterface


class PipelineMixin(
    ActAsList[StageInstance, StageInstanceCollection],
    ImplementsInterface,
    ABC,
):
    stage_instances: StageInstanceCollection

    def __init__(
        self,
        stage_instances: Optional[StageInstanceCollection] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "stage_instances"):
            self.stage_instances = tuple()

        if stage_instances:
            self.stage_instances = stage_instances

    def _get_items(self) -> StageInstanceCollection:
        return self.stage_instances

    def _set_items(self, items: StageInstanceCollection) -> Self:
        self.stage_instances = items

        return self

    def _add_item(self, item: StageInstance) -> Self:
        return self.clone({"stage_instances": tuple([*self.stage_instances, item])})

    def pipe(self, stage: StageInstance) -> Self:
        """
        Adds a single stage to the pipeline.
        """
        return self._add_item(stage)
