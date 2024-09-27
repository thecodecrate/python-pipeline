from typing import Generic, Protocol
from ...traits.with_stages.with_stages import WithStages
from ...traits.with_builderable.with_builderable import WithBuilderable
from ...traits.with_pipeline_builder.with_pipeline_builder import (
    WithPipelineBuilder,
)
from ..pipeline.payload import TPayload


class PipelineBuilderInterface(
    WithPipelineBuilder[TPayload],
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    pass
