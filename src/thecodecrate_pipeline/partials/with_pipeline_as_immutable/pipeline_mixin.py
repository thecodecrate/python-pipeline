from typing import Protocol

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_item import PipelineItem
from ...support.renamable_list.traits.has_immutability import (
    HasImmutability as HasImmutabilityConcern,
)


class PipelineMixin(
    HasImmutabilityConcern[PipelineItem[TPayload, ...]],
    ImplementsPipelineInterface[TPayload],
    Protocol[TPayload],
):
    pass
