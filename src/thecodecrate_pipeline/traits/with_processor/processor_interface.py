from abc import ABC, abstractmethod
from typing import Generic

from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class ProcessorInterface(
    Generic[TPayload],
    ABC,
):
    @abstractmethod
    def process(
        self,
        stages: list[PipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        pass
