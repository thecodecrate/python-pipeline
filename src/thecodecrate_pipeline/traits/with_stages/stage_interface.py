from abc import ABC, abstractmethod
from typing import Callable, Generic
from ...core.pipeline.payload import TPayload


class StageInterface(
    Generic[TPayload],
    ABC,
):
    @abstractmethod
    def __call__(self, payload: TPayload) -> TPayload:
        pass


StageOrCallable = StageInterface[TPayload] | Callable[[TPayload], TPayload]
