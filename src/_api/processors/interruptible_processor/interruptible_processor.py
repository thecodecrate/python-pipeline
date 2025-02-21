import inspect
from typing import Any, Awaitable, Callable, cast

from ...core import Processor, StageInstanceCollection, T_in, T_out

CheckCallable = Callable[[T_in], bool | Awaitable[bool]]


class InterruptibleProcessor(Processor[T_in, T_out]):
    """Processor with conditional interruption."""

    check: CheckCallable[T_in]
    """Callable for processing interruption. Useful for declarative subclassing.

    Example:
        ```python
        class MaxValueProcessor(InterruptibleProcessor[int, int]):
            # interrupt if value exceeds 100
            check = lambda x: x > 100
        ```
    """

    def __init__(self, check: CheckCallable[T_in]) -> None:
        """Constructor.

        Parameters:
            check: Callable for processing interruption.

        Example:
            ```python
            # Interrupts when payload value exceeds 100
            def check_value(payload: int) -> bool:
                return payload > 100

            # Create processor with the check
            processor = InterruptibleProcessor(check_value)

            # Process payload - will stop if value exceeds 100
            result = await processor.process(initial_payload, stages)
            ```
        """
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

            if await self._call_check(payload):
                return cast(T_out, payload)

        return cast(T_out, payload)

    async def _call_check(self, payload: T_in) -> bool:
        result = self.check(payload)

        if inspect.isawaitable(result):
            return await result

        return result
