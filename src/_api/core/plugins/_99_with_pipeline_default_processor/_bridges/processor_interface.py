from typing import Protocol

# extends: outside base
from ..._06_with_pipeline_processor import (
    ProcessorInterface as ProcessorBaseInterface,
)

# uses: bridge interface
from .types import T_in, T_out


class ProcessorInterface(
    ProcessorBaseInterface,
    Protocol[T_in, T_out],
):
    pass
