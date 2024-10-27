from typing import Any, Callable, Protocol


class HasCallAsyncInterface(Protocol):
    async def _call_async(
        self, callable_: Callable[..., Any], *args: Any, **kwds: Any
    ) -> Any: ...
