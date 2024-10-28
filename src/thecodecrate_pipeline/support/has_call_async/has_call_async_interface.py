from typing import Any, Awaitable, Callable, Protocol, TypeVar

TCallableReturn = TypeVar("TCallableReturn", infer_variance=True)


class HasCallAsyncInterface(Protocol):
    async def _call(
        self,
        callable: Callable[..., TCallableReturn | Awaitable[TCallableReturn]],
        *args: Any,
        **kwds: Any,
    ) -> TCallableReturn: ...
