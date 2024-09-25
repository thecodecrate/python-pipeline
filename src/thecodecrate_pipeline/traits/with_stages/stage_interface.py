from abc import ABC, abstractmethod
from typing import Generic

from ...core.pipeline.payload import TPayload


class StageInterface(
    Generic[TPayload],
    ABC,
):
    @abstractmethod
    def __call__(self, payload: TPayload) -> TPayload:
        pass
