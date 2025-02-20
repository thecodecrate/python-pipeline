from typing import Generic

# extends: outside base
from ..._06_with_pipeline_processor import (
    Processor as ProcessorBase,
)

# implements: self-interface
from .processor_interface import ProcessorInterface as ImplementsInterface

# uses: bridge interface
from .types import T_in, T_out


class Processor(
    ProcessorBase[T_in, T_out],
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
