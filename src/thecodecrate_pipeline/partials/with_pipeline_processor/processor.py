from abc import ABC, abstractmethod
import inspect
from typing import Any

from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class Processor(
    ImplementsProcessorInterface[T_in, T_out],
    ABC,
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        pass

    async def _call_stage(
        self,
        payload: T_in,
        stage: StageCallableType,
        *args: Any,
        **kwds: Any,
    ) -> T_in:
        result = stage(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
