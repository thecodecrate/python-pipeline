from typing import Any, Protocol, Self

from .command_interface import CommandInterface
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType
from ..with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)


class ProcessorInterfaceMixin(
    WithProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    def set_command_class(
        self, command_class: type[CommandInterface[T_in, T_out]]
    ) -> Self: ...

    def get_command_class(
        self,
    ) -> type[CommandInterface[T_in, T_out]] | None: ...

    def make_command(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> CommandInterface[T_in, T_out]: ...

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
