from abc import abstractmethod
import inspect
from typing import Any, Callable

from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..with_base.payload_type import TPayload
from ..with_base.stage_callable import StageCallable

CallableAsyncOrSync = Callable[..., Any]


class Processor(
    ImplementsProcessorInterface[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        stages: list[StageCallable[TPayload]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass

    async def _call_stage(
        self,
        payload: TPayload,
        stage: StageCallable[TPayload],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        result = stage(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
