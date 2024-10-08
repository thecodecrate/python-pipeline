from typing import Self

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.payload_type import TPayload
from ..with_base.stage_callable import StageCallable
from ...support.renamable_list.renamable_list import (
    RenamableList as RenamableListConcern,
)


class PipelineMixin(
    RenamableListConcern[StageCallable[TPayload]],
    ImplementsPipelineInterface[TPayload],
):
    stage_instances: list[StageCallable[TPayload]] = []

    def get_items(self) -> list[StageCallable[TPayload]]:
        return self.stage_instances

    def set_items(self, items: list[StageCallable[TPayload]]) -> Self:
        self.stage_instances = items

        return self
