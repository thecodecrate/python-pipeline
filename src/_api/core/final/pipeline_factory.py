from typing import Generic, Optional

from ..partials.step01_base.pipeline_interface import TPipeline
from ..partials.step05_pipeline_factory import PipelineFactory_Base
from ..partials.step06_pipeline_processor import PipelineFactory_WithPipelineProcessor
from ..partials.step07_pipeline_default_processor import (
    PipelineFactory_WithPipelineDefaultProcessor,
)
from .pipeline import Pipeline
from .pipeline_factory_interface import PipelineFactoryInterface as ImplementsInterface
from .types import T_in, T_out


class PipelineFactory(
    PipelineFactory_WithPipelineDefaultProcessor[T_in, T_out],
    PipelineFactory_WithPipelineProcessor[T_in, T_out],
    PipelineFactory_Base,
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    _model_class: Optional[type[TPipeline]] = Pipeline
