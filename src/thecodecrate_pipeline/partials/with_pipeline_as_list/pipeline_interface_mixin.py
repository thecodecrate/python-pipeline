from typing import Protocol

from ..with_base.stage_callable import StageCallableType
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ...support.renamable_list.renamable_list_interface import (
    RenamableListInterface,
)


class PipelineInterfaceMixin(
    RenamableListInterface[StageCallableType],
    WithPipelineBaseInterface,
    Protocol,
):
    pass
