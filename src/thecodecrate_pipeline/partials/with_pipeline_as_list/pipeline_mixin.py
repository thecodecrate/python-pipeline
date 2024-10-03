from typing import Protocol, Self

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)
from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_item import PipelineItem
from ...support.renamable_list.renamable_list import (
    RenamableList as RenamableListConcern,
)


class PipelineMixin(
    RenamableListConcern[PipelineItem[TPayload, ...]],
    PipelineInterface[TPayload],
    Protocol[TPayload],
):
    stages: list[PipelineItem[TPayload, ...]] = []

    def get_items(self) -> list[PipelineItem[TPayload, ...]]:
        return self.stages

    def set_items(self, items: list[PipelineItem[TPayload, ...]]) -> Self:
        self.stages = items

        return self
