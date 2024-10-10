from abc import ABC

from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_base.types import T_in, T_out
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorBaseConcern,
)
from ..partials.with_processor_commands.processor_mixin import (
    ProcessorMixin as WithProcessorCommandsConcern,
)


class Processor(
    WithProcessorCommandsConcern[T_in, T_out],
    WithProcessorBaseConcern[T_in, T_out],
    ImplementsProcessorInterface[T_in, T_out],
    ABC,
):
    pass
