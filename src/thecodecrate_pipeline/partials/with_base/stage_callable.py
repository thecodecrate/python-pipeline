from typing import Any, Awaitable, Protocol

from .payload_type import TPayload


class StageCallable(Protocol[TPayload]):
    def __call__(
        self,
        payload: TPayload,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> TPayload | Awaitable[TPayload]: ...
