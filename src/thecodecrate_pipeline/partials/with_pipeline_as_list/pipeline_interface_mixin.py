from typing import Protocol

from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_callable import PipelineCallable
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ...support.renamable_list.renamable_list_interface import (
    RenamableListInterface,
)


class PipelineInterfaceMixin(
    RenamableListInterface[PipelineCallable[TPayload, ...]],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    pass
