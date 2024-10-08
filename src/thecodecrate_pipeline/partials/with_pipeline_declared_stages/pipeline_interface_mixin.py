from typing import Protocol

from ..with_base.payload_type import TPayload
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    def _instantiate_stages(self) -> None: ...
