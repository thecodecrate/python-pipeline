from abc import ABC
from typing import Any, Generic, Optional

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

    def __init__(
        self,
        command_class: Optional[type[CommandInterface[T_in, T_out]]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        self.command_class = command_class or self.command_class

    def _make_command(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> CommandInterface[T_in, T_out]:
        if self.command_class is None:
            raise ValueError("Command class not set")

        return self.command_class(
            processor=self, payload=payload, stages=stages, *args, **kwds
        )

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        command = self._make_command(payload, stages, *args, **kwds)

        return await command.execute()
