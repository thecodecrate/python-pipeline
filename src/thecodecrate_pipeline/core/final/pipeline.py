from ...processors.chained_processor.chained_processor import ChainedProcessor
from ..partials.step01_base.pipeline import (
    Pipeline as WithPipelineBaseConcern,
)
from ..partials.step01_base.types import T_in, T_out
from ..partials.step02_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsListConcern,
)
from ..partials.step04_pipeline_declared_stages.pipeline_mixin import (
    PipelineMixin as WithPipelineDeclaredStagesConcern,
)
from ..partials.step06_pipeline_processor.pipeline_mixin import (
    PipelineMixin as WithPipelineProcessorConcern,
)
from ..partials.step07_pipeline_as_stage.pipeline_mixin import (
    PipelineMixin as WithPipelineAsStageConcern,
)
from .pipeline_interface import (
    PipelineInterface as ImplementsPipelineInterface,
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
