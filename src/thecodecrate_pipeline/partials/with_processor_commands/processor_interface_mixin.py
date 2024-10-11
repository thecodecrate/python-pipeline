from typing import Any, Optional, Protocol

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
    def __init__(
        self,
        command_class: Optional[type[CommandInterface[T_in, T_out]]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def _make_command(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> CommandInterface[T_in, T_out]: ...
