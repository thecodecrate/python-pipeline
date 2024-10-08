from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.payload_type import TPayload
from ..with_base.stage_callable import StageCallable
from ...support.renamable_list.traits.has_immutability import (
    HasImmutability as HasImmutabilityConcern,
)


class PipelineMixin(
    HasImmutabilityConcern[StageCallable[TPayload]],
    ImplementsPipelineInterface[TPayload],
):
    pass
