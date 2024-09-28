from typing import Protocol
from thecodecrate_builderable import WithImmutableParts

from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class WithImmutability(
    WithImmutableParts[TPayload, PipelineCallable[TPayload, ...]],
    Protocol[TPayload],
):
    pass
