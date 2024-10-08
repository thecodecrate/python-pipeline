from .pipeline import Pipeline
from .pipeline_builder_interface import (
    PipelineBuilderInterface as ImplementsPipelineBuilderInterface,
)
from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.pipeline import (
    Pipeline as WithPipelineBaseConcern,
)
from ..partials.with_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsListConcern,
)
from ..partials.with_builder_methods.pipeline_mixin import (
    PipelineMixin as WithBuilderMethodsConcern,
)


class PipelineBuilder(
    WithBuilderMethodsConcern[Pipeline[T_in, T_out], T_in, T_out],
    WithPipelineAsListConcern,
    WithPipelineBaseConcern,
    ImplementsPipelineBuilderInterface[T_in, T_out],
):
    pipelineable_class = Pipeline
