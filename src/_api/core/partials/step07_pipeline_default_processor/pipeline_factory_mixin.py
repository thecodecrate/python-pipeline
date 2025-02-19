from typing import Generic, Optional

from ..step01_base import Pipeline_Base_Interface, T_in, T_out, TPipeline
from ..step05_pipeline_factory import PipelineFactory_Base
from ..step06_pipeline_processor import PipelineFactory_WithPipelineProcessor
from .pipeline_factory_interface_mixin import (
    PipelineFactoryInterfaceMixin as ImplementsInterface,
)
from .pipeline_mixin import PipelineMixin as Pipeline


class PipelineFactory(
    PipelineFactory_WithPipelineProcessor[T_in, T_out],
    PipelineFactory_Base[Pipeline_Base_Interface],
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    _model_class: Optional[type[TPipeline]] = Pipeline
