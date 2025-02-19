from typing import Generic

from ..partials.step01_base import Pipeline_Base
from ..partials.step02_pipeline_as_list import Pipeline_WithPipelineAsList
from ..partials.step04_pipeline_declared_stages import (
    Pipeline_WithPipelineDeclaredStages,
)
from ..partials.step06_pipeline_processor import Pipeline_WithPipelineProcessor
from ..partials.step07_pipeline_default_processor import (
    Pipeline_WithPipelineDefaultProcessor,
)
from ..partials.step08_pipeline_as_stage import Pipeline_WithPipelineAsStage
from .pipeline_interface import PipelineInterface as ImplementsInterface
from .types import T_in, T_out


class Pipeline(
    Pipeline_WithPipelineAsStage[T_in, T_out],
    Pipeline_WithPipelineDefaultProcessor[T_in, T_out],
    Pipeline_WithPipelineProcessor[T_in, T_out],
    Pipeline_WithPipelineDeclaredStages,
    Pipeline_WithPipelineAsList,
    Pipeline_Base,
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
