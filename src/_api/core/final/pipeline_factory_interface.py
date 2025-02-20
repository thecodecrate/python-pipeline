from typing import Protocol

# extends: outside base
from ..plugins._05_with_pipeline_factory import (
    PipelineFactoryInterface as PipelineFactoryBaseInterface,
)

# extends: outside mixins
from ..plugins._06_with_pipeline_processor import (
    PipelineFactoryInterfaceMixin as _06_WithPipelineProcessorInterface,
)
from ..plugins._99_with_pipeline_default_processor import (
    PipelineFactoryInterfaceMixin as _99_WithPipelineDefaultProcessorInterface,
)

# uses: bridge interface
from .pipeline_interface import PipelineInterface
from .types import T_in, T_out


class PipelineFactoryInterface(
    _99_WithPipelineDefaultProcessorInterface[T_in, T_out],
    _06_WithPipelineProcessorInterface[T_in, T_out],
    PipelineFactoryBaseInterface[PipelineInterface[T_in, T_out]],
    Protocol[T_in, T_out],
):
    pass
