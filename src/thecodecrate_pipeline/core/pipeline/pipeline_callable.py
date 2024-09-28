from typing import Awaitable, Callable, Concatenate, ParamSpec
from ...core.pipeline.payload import TPayload
from ...traits.with_stages.stage_interface import StageInterface

TArgs = ParamSpec("TArgs")  # To capture *args and **kwds

PipelineCallable = (
    StageInterface[TPayload]
    | Callable[Concatenate[TPayload, TArgs], Awaitable[TPayload]]
    | Callable[Concatenate[TPayload, TArgs], TPayload]
)
