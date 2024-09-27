from abc import abstractmethod
from typing import Generic, Protocol
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class ProcessorInterface(
    Generic[TPayload],
    Protocol,
):
    @abstractmethod
    def process(
        self,
        stages: list[PipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        pass
