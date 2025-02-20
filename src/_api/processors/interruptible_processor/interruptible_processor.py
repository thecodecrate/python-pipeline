import inspect
from typing import Any, Awaitable, Callable, cast

from ...core import Processor, StageInstanceCollection, T_in, T_out

CheckCallable = Callable[[T_in], bool | Awaitable[bool]]


class InterruptibleProcessor(Processor[T_in, T_out]):
    check: CheckCallable[T_in]

    def __init__(self, check: CheckCallable[T_in]) -> None:
        super().__init__()

        self.check = check

    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call(callable=stage, payload=payload, *args, **kwds)

            if not await self._call_check(payload):
                return cast(T_out, payload)

        return cast(T_out, payload)

    async def _call_check(self, payload: T_in) -> bool:
        result = self.check(payload)

        if inspect.isawaitable(result):
            return await result

        return result
