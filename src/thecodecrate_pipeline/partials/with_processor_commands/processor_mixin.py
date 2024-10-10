from abc import ABC
from typing import Any, Generic, Optional, Self

from .command_interface import CommandInterface
from .processor_interface_mixin import (
    ProcessorInterfaceMixin as ImplementsProcessorInterface,
)
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class ProcessorMixin(
    ImplementsProcessorInterface[T_in, T_out],
    Generic[T_in, T_out],
    ABC,
):
    command_class: Optional[type[CommandInterface[T_in, T_out]]] = None

    def set_command_class(
        self, command_class: type[CommandInterface[T_in, T_out]]
    ) -> Self:
        self.command_class = command_class

        return self

    def get_command_class(self) -> type[CommandInterface[T_in, T_out]] | None:
        return self.command_class

    def make_command(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> CommandInterface[T_in, T_out]:
        if self.command_class is None:
            raise ValueError("Command class not set")

        return self.command_class(
            processor=self,
            payload=payload,
            stages=stages,
            *args,
            **kwds,
        )

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        command = self.make_command(payload, stages, *args, **kwds)

        return await command.execute()
