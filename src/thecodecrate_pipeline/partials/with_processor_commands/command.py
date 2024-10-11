from abc import ABC, abstractmethod
import inspect
from typing import Any, Generic

from .processor_facade import TProcessor
from .command_interface import CommandInterface
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class Command(
    CommandInterface[T_in, T_out],
    Generic[TProcessor, T_in, T_out],
    ABC,
):
    processor: TProcessor
    payload: T_in
    stages: list[StageCallableType]
    extra_args: Any = None
    extra_kwds: Any = None

    def __init__(
        self,
        processor: TProcessor,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> None:
        self.processor = processor
        self.payload = payload
        self.stages = stages.copy()
        self.extra_args = args
        self.extra_kwds = kwds

    @abstractmethod
    async def execute(self) -> T_out:
        pass

    async def _call_stage(
        self, payload: T_in, stage: StageCallableType, *args: Any, **kwds: Any
    ) -> T_in:
        result = stage(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
