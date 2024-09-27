from typing import Generic, Protocol
from thecodecrate_builderable import WithParts
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload


class WithBuilderable(
    WithParts[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    Protocol,
):
    pass
