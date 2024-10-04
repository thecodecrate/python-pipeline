from typing import Self

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_callable import PipelineCallable
from ...support.renamable_list.renamable_list import (
    RenamableList as RenamableListConcern,
)


class PipelineMixin(
    RenamableListConcern[PipelineCallable[TPayload, ...]],
    ImplementsPipelineInterface[TPayload],
):
    stage_instances: list[PipelineCallable[TPayload, ...]] = []

    def get_items(self) -> list[PipelineCallable[TPayload, ...]]:
        return self.stage_instances

    def set_items(self, items: list[PipelineCallable[TPayload, ...]]) -> Self:
        self.stage_instances = items

        return self
