from typing import Generic

from .pipeline_interface import PipelineInterface
from ..partials.with_base.type_payload import TPayload
from ..processors.chained_processor import ChainedProcessor
from ..partials.with_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsListConcern,
)
from ..partials.with_pipeline_processor.pipeline_mixin import (
    PipelineMixin as WithPipelineProcessorConcern,
)
from ..partials.with_pipeline_as_stage.pipeline_mixin import (
    PipelineMixin as WithPipelineAsStageConcern,
)
from ..partials.with_pipeline_as_immutable.pipeline_mixin import (
    PipelineMixin as WithPipelineAsImmutableConcern,
)
from ..partials.with_pipelineable_methods.pipeline_mixin import (
    PipelineMixin as WithPipelineableMethodsConcern,
)


class Pipeline(
    WithPipelineableMethodsConcern[TPayload],
    WithPipelineAsImmutableConcern[TPayload],
    WithPipelineAsStageConcern[TPayload],
    WithPipelineProcessorConcern[TPayload],
    WithPipelineAsListConcern[TPayload],
    PipelineInterface[TPayload],
    Generic[TPayload],
):
    processor_class = ChainedProcessor
