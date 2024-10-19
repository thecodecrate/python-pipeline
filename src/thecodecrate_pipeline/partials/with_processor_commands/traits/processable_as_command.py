from typing import Any, Optional, cast

from ...with_base.types import T_in, T_out
from ..processor_mixin import ProcessorMixin as Processor
from ..strategies.command_processing_strategy import CommandProcessingStrategy
from ..pipeline_interface_mixin import PipelineInterfaceMixin


class ProcessableAsCommand(PipelineInterfaceMixin[T_in, T_out]):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        self.processor = cast(
            Optional[Processor], self.processor
        )  # type: ignore

        super().__init__(*args, **kwds)  # type: ignore

        if self.processor:
            self.processor.with_processing_strategy(
                CommandProcessingStrategy(
                    self.processor, self.processor.command_class
                )
            )
