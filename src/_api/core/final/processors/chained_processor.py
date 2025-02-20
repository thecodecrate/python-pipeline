from typing import Generic

# extends: outside base
from ...plugins._99_with_pipeline_default_processor import (
    ChainedProcessor as ChainedProcessorBase,
)

# uses: bridge interface
from ..types import T_in, T_out


class ChainedProcessor(
    ChainedProcessorBase[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
