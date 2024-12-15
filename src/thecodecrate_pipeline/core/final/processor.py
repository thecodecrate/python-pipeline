from abc import ABC

from ..partials.step01_base.types import T_in, T_out
from ..partials.step06_pipeline_processor.processor import (
    Processor as WithProcessorBaseConcern,
)
from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)


class Processor(
    WithProcessorBaseConcern[T_in, T_out],
    ImplementsProcessorInterface[T_in, T_out],
    ABC,
):
    pass
