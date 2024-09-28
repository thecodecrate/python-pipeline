from abc import abstractmethod
from typing import Any, Protocol
from ...core.pipeline.payload import TPayload


class StageInterface(Protocol[TPayload]):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass
