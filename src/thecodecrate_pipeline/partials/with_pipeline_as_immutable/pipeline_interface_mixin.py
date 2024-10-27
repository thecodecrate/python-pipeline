from typing import Protocol

from ..with_base.stage_callable import StageCallableType
from ...support.act_as_list import HasListImmutabilityInterface
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)


class PipelineInterfaceMixin(
    HasListImmutabilityInterface[StageCallableType],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol,
):
    pass
