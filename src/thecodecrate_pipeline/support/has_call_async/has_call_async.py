import inspect
from typing import Any, Callable, Protocol, TypeVar

from .has_call_async_interface import HasCallAsyncInterface

TCallableReturn = TypeVar("TCallableReturn", infer_variance=True)


class HasCallAsync(HasCallAsyncInterface, Protocol):
    async def _call_async(
        self,
        callable_: Callable[..., TCallableReturn],
        *args: Any,
        **kwds: Any,
    ) -> TCallableReturn:
        result = callable_(*args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
