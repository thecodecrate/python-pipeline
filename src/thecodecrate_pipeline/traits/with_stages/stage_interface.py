from abc import abstractmethod
from typing import Any, Generic, Protocol
from ...core.pipeline.payload import TPayload


class StageInterface(
    Generic[TPayload],
    Protocol,
):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass
