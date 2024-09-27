from typing import Awaitable, Callable
from ...core.pipeline.payload import TPayload
from ...traits.with_stages.stage_interface import StageInterface

PipelineCallable = (
    StageInterface[TPayload]
    | Callable[[TPayload], Awaitable[TPayload]]
    | Callable[[TPayload], TPayload]
)
