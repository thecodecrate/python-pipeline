from abc import ABC

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.stage_callable import StageCallableType
from ...support.act_as_list import HasListImmutability


class PipelineMixin(
    HasListImmutability[StageCallableType],
    ImplementsPipelineInterface,
    ABC,
):
    pass
