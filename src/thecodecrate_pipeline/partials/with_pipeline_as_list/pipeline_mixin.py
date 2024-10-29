from abc import ABC
from typing import Any, Optional, Self

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.stage_callable import StageCallableType
from ...support.act_as_list import ActAsList


class PipelineMixin(
    ActAsList[StageCallableType],
    ImplementsPipelineInterface,
    ABC,
):
    stage_instances: list[StageCallableType]

    def __init__(
        self,
        stage_instances: Optional[list[StageCallableType]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "stage_instances"):
            self.stage_instances = []

        if stage_instances:
            self.stage_instances = [*stage_instances]

    def _get_items(self) -> list[StageCallableType]:
        return self.stage_instances

    def _set_items(self, items: list[StageCallableType]) -> Self:
        self.stage_instances = items

        return self

    def pipe(self, stage: StageCallableType) -> Self:
        return self._add_item(stage)
