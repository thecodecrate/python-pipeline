from typing import Protocol

from ..partials.step01_base import Pipeline_Base_Interface
from ..partials.step02_pipeline_as_list import Pipeline_WithPipelineAsList_Interface
from ..partials.step04_pipeline_declared_stages import (
    Pipeline_WithPipelineDeclaredStages_Interface,
)
from ..partials.step06_pipeline_processor import (
    Pipeline_WithPipelineProcessor_Interface,
)
from ..partials.step07_pipeline_default_processor import (
    Pipeline_WithPipelineDefaultProcessor_Interface,
)
from ..partials.step08_pipeline_as_stage import Pipeline_WithPipelineAsStage_Interface
from .types import T_in, T_out


class PipelineInterface(
    Pipeline_WithPipelineAsStage_Interface[T_in, T_out],
    Pipeline_WithPipelineDefaultProcessor_Interface[T_in, T_out],
    Pipeline_WithPipelineProcessor_Interface[T_in, T_out],
    Pipeline_WithPipelineDeclaredStages_Interface,
    Pipeline_WithPipelineAsList_Interface,
    Pipeline_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
