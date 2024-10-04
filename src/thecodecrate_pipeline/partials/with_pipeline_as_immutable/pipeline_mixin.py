from typing import Protocol

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_callable import PipelineCallable
from ...support.renamable_list.traits.has_immutability import (
    HasImmutability as HasImmutabilityConcern,
)


class PipelineMixin(
    HasImmutabilityConcern[PipelineCallable[TPayload, ...]],
    ImplementsPipelineInterface[TPayload],
    Protocol[TPayload],
):
    pass
