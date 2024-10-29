from .pipeline_interface import (
    PipelineInterface as ImplementsPipelineInterface,
)
from ..processors.chained_processor.chained_processor import ChainedProcessor
from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.pipeline import (
    Pipeline as WithPipelineBaseConcern,
)
from ..partials.with_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsListConcern,
)
from ..partials.with_pipeline_declared_stages.pipeline_mixin import (
    PipelineMixin as WithPipelineDeclaredStagesConcern,
)
from ..partials.with_pipeline_processor.pipeline_mixin import (
    PipelineMixin as WithPipelineProcessorConcern,
)
from ..partials.with_pipeline_as_stage.pipeline_mixin import (
    PipelineMixin as WithPipelineAsStageConcern,
)


class Pipeline(
    WithPipelineAsStageConcern[T_in, T_out],
    WithPipelineProcessorConcern[T_in, T_out],
    WithPipelineDeclaredStagesConcern,
    WithPipelineAsListConcern,
    WithPipelineBaseConcern,
    ImplementsPipelineInterface[T_in, T_out],
):
    processor_class = ChainedProcessor
