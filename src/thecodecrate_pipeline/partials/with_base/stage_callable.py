from typing import Any, Awaitable, Protocol

from .types import T_in, T_out


class StageCallable(Protocol[T_in, T_out]):
    def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out | Awaitable[T_out]: ...


StageCallableType = StageCallable[Any, Any]
