from typing import Awaitable, Callable, Concatenate, ParamSpec

from .type_payload import TPayload

TArgs = ParamSpec("TArgs")  # capture *args and **kwds

PipelineItem = (
    Callable[Concatenate[TPayload, TArgs], Awaitable[TPayload]]
    | Callable[Concatenate[TPayload, TArgs], TPayload]
)
