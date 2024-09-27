from typing import Generic, Protocol
from thecodecrate_builderable import (
    WithImmutability as BuilderableWithImmutability,
)
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class WithImmutability(
    BuilderableWithImmutability[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    Protocol,
):
    pass
