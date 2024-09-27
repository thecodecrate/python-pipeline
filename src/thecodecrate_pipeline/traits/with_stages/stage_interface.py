from abc import abstractmethod
from typing import Generic, Protocol
from ...core.pipeline.payload import TPayload


class StageInterface(
    Generic[TPayload],
    Protocol,
):
    @abstractmethod
    def __call__(self, payload: TPayload) -> TPayload:
        pass
