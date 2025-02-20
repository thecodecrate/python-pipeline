from typing import Protocol

# extends: outside base
from ...plugins._99_with_pipeline_default_processor import (
    ChainedProcessorInterface as ChainedProcessorBaseInterface,
)

# uses: final interface
from ..types import T_in, T_out


class ChainedProcessorInterface(
    ChainedProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
