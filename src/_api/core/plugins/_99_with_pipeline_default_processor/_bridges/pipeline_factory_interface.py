from typing import Protocol

# extends: outside base
from ..._05_with_pipeline_factory import (
    PipelineFactoryInterface as PipelineFactoryBaseInterface,
)

# extends: outside mixins
from ..._06_with_pipeline_processor import (
    PipelineFactoryInterfaceMixin as _06_WithPipelineProcessorInterface,
)

# uses: bridge interface
from .pipeline_interface import PipelineInterface
from .types import T_in, T_out


class PipelineFactoryInterface(
    _06_WithPipelineProcessorInterface[T_in, T_out],
    PipelineFactoryBaseInterface[PipelineInterface[T_in, T_out]],
    Protocol[T_in, T_out],
):
    pass
