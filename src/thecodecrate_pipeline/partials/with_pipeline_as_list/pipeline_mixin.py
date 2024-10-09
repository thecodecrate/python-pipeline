from abc import ABC
from typing import Self

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
    stage_instances: list[StageCallableType] = []

    def get_items(self) -> list[StageCallableType]:
        return self.stage_instances

    def set_items(self, items: list[StageCallableType]) -> Self:
        self.stage_instances = items

        return self
