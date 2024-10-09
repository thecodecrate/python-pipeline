import inspect
from typing import Any, Awaitable, Callable, cast

from ...classes.stage_callable import StageCallable
from ...classes.types import T_in, T_out
from ...classes.processor import Processor

CheckCallable = Callable[[T_in], bool | Awaitable[bool]]


class InterruptibleProcessor(Processor[T_in, T_out]):
    check: CheckCallable[T_in]

    def __init__(self, check: CheckCallable[T_in]) -> None:
        self.check = check

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call_stage(
                payload=payload, stage=stage, *args, **kwds
            )

            if not await self._call_check(payload):
                return cast(T_out, payload)

        return cast(T_out, payload)

    async def _call_check(self, payload: T_in) -> bool:
        result = self.check(payload)

        if inspect.isawaitable(result):
            return await result

        return result
