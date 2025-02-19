from typing import Protocol

from ..partials.step06_pipeline_processor import Processor_Base_Interface
from .types import T_in, T_out


class ProcessorInterface(
    Processor_Base_Interface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
