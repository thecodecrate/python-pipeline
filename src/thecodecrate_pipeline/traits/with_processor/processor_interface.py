from abc import ABC, abstractmethod
from typing import Generic
from ...core.pipeline.payload import TPayload
from ...traits.with_stages.stage_interface import StageOrCallable


class ProcessorInterface(
    Generic[TPayload],
    ABC,
):
    @abstractmethod
    def process(
        self,
        stages: list[StageOrCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        pass
