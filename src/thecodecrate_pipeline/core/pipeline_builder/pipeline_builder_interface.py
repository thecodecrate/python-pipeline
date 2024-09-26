from abc import ABC
from typing import Generic
from thecodecrate_builderable import Builderable

from ...traits.with_stages.with_stages import WithStages
from ...traits.with_pipeline_builder.with_pipeline_builder import (
    WithPipelineBuilder,
)
from ..pipeline.pipeline_callable import PipelineCallable
from ..pipeline.payload import TPayload


class PipelineBuilderInterface(
    WithPipelineBuilder["PipelineBuilderInterface[TPayload]", TPayload],
    WithStages["PipelineBuilderInterface[TPayload]", TPayload],
    Builderable[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass
