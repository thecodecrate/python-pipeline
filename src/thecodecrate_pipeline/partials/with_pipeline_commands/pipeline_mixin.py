from abc import ABC
from typing import Any, Generic, Optional, Self, cast

from .command_facade import TCommand
from .processor_facade import ProcessorFacade
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    ImplementsPipelineInterface[TCommand, T_in, T_out],
    Generic[TCommand, T_in, T_out],
    ABC,
):
    command_class: Optional[type[TCommand]] = None

    def set_command_class(self, command_class: type[TCommand]) -> Self:
        self.command_class = command_class

        return self

    def get_command_class(self) -> type[TCommand] | None:
        return self.command_class

    def make_command_processor(self) -> ProcessorFacade:
        if self.command_class is None:
            raise ValueError("Command class not set")

        processor_class = self.get_base_processor_class()

        processor = cast(ProcessorFacade, processor_class())

        processor.set_command_class(self.command_class)

        return processor

    def ensure_command_processor_is_set(self) -> ProcessorFacade:
        processor = cast(ProcessorFacade, self.get_processor())

        if processor.get_command_class() != self.command_class:
            processor = self.make_command_processor()

            self.set_processor(processor)

        return processor

    async def process(
        self,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        if self.command_class is not None:
            self.ensure_command_processor_is_set()

        # ignoring linter error, on runtime "super()" is implemented
        return await super().process(payload, *args, **kwds)  # type: ignore
