from abc import abstractmethod
from typing import Any, Protocol

from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class ProcessorInterface(
    Protocol[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    async def _call_stage(
        self,
        payload: T_in,
        stage: StageCallableType,
        *args: Any,
        **kwds: Any,
    ) -> T_in: ...
