from typing import Generic

from .pipeline import Pipeline
from ..partials.with_base.types import T_in, T_out
from ..partials.with_pipeline_factory.pipeline_factory import (
    PipelineFactory as WithPipelineFactoryBaseConcern,
)
from .pipeline_factory_interface import (
    PipelineFactoryInterface as ImplementsPipelineFactoryInterface,
)
from ..partials.with_pipeline_processor.pipeline_factory_mixin import (
    PipelineFactoryMixin as WithProcessorConcern,
)


class PipelineFactory(
    WithProcessorConcern,
    WithPipelineFactoryBaseConcern[Pipeline[T_in, T_out]],
    ImplementsPipelineFactoryInterface,
    Generic[T_in, T_out],
):
    _instance_class = Pipeline
