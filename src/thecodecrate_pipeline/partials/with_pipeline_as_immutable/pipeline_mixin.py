from abc import ABC

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.stage_callable import StageCallableType
from ...support.renamable_list.traits.has_immutability import (
    HasImmutability as HasImmutabilityConcern,
)


class PipelineMixin(
    HasImmutabilityConcern[StageCallableType],
    ImplementsPipelineInterface,
    ABC,
):
    pass
