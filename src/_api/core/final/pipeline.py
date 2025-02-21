from typing import Generic

# extends: outside base
from ..plugins._01_with_base import Pipeline as PipelineBase

# extends: outside mixins
from ..plugins._02_with_pipeline_as_list import (
    PipelineMixin as _02_WithPipelineAsList,
)
from ..plugins._04_with_pipeline_declared_stages import (
    PipelineMixin as _04_WithPipelineDeclaredStages,
)
from ..plugins._06_with_pipeline_processor import (
    PipelineMixin as _06_WithPipelineProcessor,
)
from ..plugins._08_with_pipeline_as_stage import (
    PipelineMixin as _08_WithPipelineAsStage,
)
from ..plugins._99_with_pipeline_default_processor import (
    PipelineMixin as _99_WithPipelineDefaultProcessor,
)

# implements: self-interface
from .pipeline_interface import PipelineInterface as ImplementsInterface

# uses: bridge interface
from .types import T_in, T_out


class Pipeline(
    _99_WithPipelineDefaultProcessor[T_in, T_out],
    _08_WithPipelineAsStage[T_in, T_out],
    _06_WithPipelineProcessor[T_in, T_out],
    _04_WithPipelineDeclaredStages,
    _02_WithPipelineAsList,
    PipelineBase,
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    """Pipeline Class"""

    pass
