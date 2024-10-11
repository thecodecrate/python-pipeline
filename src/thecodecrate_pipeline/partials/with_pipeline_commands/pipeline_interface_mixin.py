from typing import Any, Protocol, Self

from .command_facade import TCommand
from ..with_base.types import T_in, T_out
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)


class PipelineInterfaceMixin(
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[TCommand, T_in, T_out],
):
    def set_command_class(self, command_class: type[TCommand]) -> Self: ...

    def get_command_class(
        self,
    ) -> type[TCommand] | None: ...

    async def process(
        self,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
