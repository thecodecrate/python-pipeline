import inspect
from typing import Any, Awaitable, Callable, Protocol

from .has_call_async_interface import HasCallAsyncInterface, TCallableReturn


class HasCallAsync(HasCallAsyncInterface, Protocol):
    async def _call(
        self,
        callable: Callable[..., TCallableReturn | Awaitable[TCallableReturn]],
        *args: Any,
        **kwds: Any,
    ) -> TCallableReturn:
        result = callable(*args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
