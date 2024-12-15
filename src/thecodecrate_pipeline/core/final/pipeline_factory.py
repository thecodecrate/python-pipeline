from typing import Generic

from ..partials.step01_base.types import T_in, T_out
from ..partials.step05_pipeline_factory.pipeline_factory import (
    PipelineFactory as WithPipelineFactoryBaseConcern,
)
from ..partials.step06_pipeline_processor.pipeline_factory_mixin import (
    PipelineFactoryMixin as WithProcessorConcern,
)
from .pipeline import Pipeline
from .pipeline_factory_interface import (
    PipelineFactoryInterface as ImplementsPipelineFactoryInterface,
)


class PipelineFactory(
    WithProcessorConcern,
    WithPipelineFactoryBaseConcern[Pipeline[T_in, T_out]],
    ImplementsPipelineFactoryInterface,
    Generic[T_in, T_out],
):
    _model_class = Pipeline
