from typing import Protocol

from ..with_base.types import T_in, T_out
from ..with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)
from ..with_processor_commands.processor_interface_mixin import (
    ProcessorInterfaceMixin as WithProcessorCommandsInterface,
)


class ProcessorFacade(
    WithProcessorCommandsInterface[T_in, T_out],
    WithProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
