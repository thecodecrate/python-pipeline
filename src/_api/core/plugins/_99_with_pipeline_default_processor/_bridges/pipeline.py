from typing import Generic

# extends: outside base
from ..._01_with_base import Pipeline as PipelineBase

# extends: outside mixins
from ..._02_with_pipeline_as_list import (
    PipelineMixin as _02_WithPipelineAsList,
)
from ..._04_with_pipeline_declared_stages import (
    PipelineMixin as _04_WithPipelineDeclaredStages,
)
from ..._06_with_pipeline_processor import (
    PipelineMixin as _06_WithPipelineProcessor,
)
from ..._08_with_pipeline_as_stage import (
    PipelineMixin as _08_WithPipelineAsStage,
)

# implements: self-interface
from .pipeline_interface import PipelineInterface as ImplementsInterface

# uses: bridge interface
from .types import T_in, T_out


class Pipeline(
    _08_WithPipelineAsStage[T_in, T_out],
    _06_WithPipelineProcessor[T_in, T_out],
    _04_WithPipelineDeclaredStages,
    _02_WithPipelineAsList,
    PipelineBase,
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
