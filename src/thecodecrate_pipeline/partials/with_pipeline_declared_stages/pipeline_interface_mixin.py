from typing import Protocol

from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol,
):
    def _instantiate_stages(self) -> None: ...
