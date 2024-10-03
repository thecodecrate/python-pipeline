from typing import Protocol

from ..with_base.type_payload import TPayload
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    pass
