from abc import ABC
from typing import Any, Generic, Optional

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
    base_processor_class: Optional[type[ProcessorFacade]] = None
    command_class: Optional[type[TCommand]] = None

    def __init__(self, *args: Any, **kwds: Any) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if self._should_make_command_processor():
            self.processor = self._make_command_processor()

    def _should_make_command_processor(self) -> bool:
        return (
            self.command_class is not None
            and self.base_processor_class is not None
        )

    def _make_command_processor(self) -> ProcessorFacade:
        if self.base_processor_class is None:
            raise ValueError("Base processor class not set")

        return self.base_processor_class(command_class=self.command_class)
