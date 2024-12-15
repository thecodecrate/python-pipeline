from typing import Protocol

from ..partials.step01_base.types import T_in, T_out
from ..partials.step06_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)


class ProcessorInterface(
    WithProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
