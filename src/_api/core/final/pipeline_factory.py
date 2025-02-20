from typing import Generic

# extends: outside base
from ..plugins._05_with_pipeline_factory import PipelineFactory as PipelineFactoryBase

# extends: outside mixins
from ..plugins._06_with_pipeline_processor import (
    PipelineFactoryMixin as _06_WithPipelineProcessor,
)
from ..plugins._99_with_pipeline_default_processor import (
    PipelineFactoryMixin as _99_WithPipelineDefaultProcessor,
)

# implements: self-interface
from .pipeline_factory_interface import PipelineFactoryInterface as ImplementsInterface

# uses: bridge interface
from .pipeline_interface import PipelineInterface
from .types import T_in, T_out


class PipelineFactory(
    _99_WithPipelineDefaultProcessor[T_in, T_out],
    _06_WithPipelineProcessor[T_in, T_out],
    PipelineFactoryBase[PipelineInterface[T_in, T_out]],
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
