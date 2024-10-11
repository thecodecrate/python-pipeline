from abc import abstractmethod
from typing import Any, Protocol

from .processor_facade import ProcessorFacade
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class CommandInterface(
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        processor: ProcessorFacade[T_in, T_out],
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    @abstractmethod
    async def execute(self) -> T_out: ...

    async def _call_stage(
        self, payload: T_in, stage: StageCallableType, *args: Any, **kwds: Any
    ) -> T_in: ...
