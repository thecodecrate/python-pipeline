from typing import Protocol

# extends: outside base
from ..._05_with_pipeline_factory import (
    PipelineFactoryInterface as PipelineFactoryBaseInterface,
)
from .._bridges.pipeline_interface import PipelineInterface

# uses: bridge interface
from .._bridges.types import T_in, T_out


class PipelineFactoryInterface(
    PipelineFactoryBaseInterface[PipelineInterface],
    Protocol[T_in, T_out],
):
    pass
