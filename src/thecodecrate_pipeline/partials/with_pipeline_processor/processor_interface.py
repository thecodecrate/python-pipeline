from abc import abstractmethod
from typing import Any, Protocol

from ..with_base.payload_type import TPayload
from ..with_base.stage_callable import StageCallable


class ProcessorInterface(
    Protocol[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        stages: list[StageCallable[TPayload]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...

    async def _call_stage(
        self,
        payload: TPayload,
        stage: StageCallable[TPayload],
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...
