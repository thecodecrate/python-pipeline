from typing import Protocol, Self

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
    Protocol[TPayload],
):
    stages: list[PipelineCallable[TPayload, ...]] = []

    def get_items(self) -> list[PipelineCallable[TPayload, ...]]:
        return self.stages

    def set_items(self, items: list[PipelineCallable[TPayload, ...]]) -> Self:
        self.stages = items

        return self
