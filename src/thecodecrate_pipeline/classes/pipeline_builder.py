from typing import Generic

from .pipeline import Pipeline
from .pipeline_builder_interface import PipelineBuilderInterface
from ..partials.with_base.type_payload import TPayload
from ..partials.with_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsListConcern,
)
from ..partials.with_builder_methods.pipeline_mixin import (
    PipelineMixin as WithBuilderMethodsConcern,
)


class PipelineBuilder(
    WithBuilderMethodsConcern[TPayload, Pipeline[TPayload]],
    WithPipelineAsListConcern[TPayload],
    PipelineBuilderInterface[TPayload],
    Generic[TPayload],
):
    pipelineable_class = Pipeline
