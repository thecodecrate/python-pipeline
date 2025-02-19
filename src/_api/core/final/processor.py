from abc import ABC

from ..partials.step06_pipeline_processor import Processor_Base
from .processor_interface import ProcessorInterface as ImplementsInterface
from .types import T_in, T_out


class Processor(
    Processor_Base[T_in, T_out],
    ImplementsInterface[T_in, T_out],
    ABC,
):
    pass
