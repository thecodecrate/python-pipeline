from typing import Protocol

from ..with_base.payload_type import TPayload
from ..with_base.stage_callable import StageCallable
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ...support.renamable_list.renamable_list_interface import (
    RenamableListInterface,
)


class PipelineInterfaceMixin(
    RenamableListInterface[StageCallable[TPayload]],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    pass
