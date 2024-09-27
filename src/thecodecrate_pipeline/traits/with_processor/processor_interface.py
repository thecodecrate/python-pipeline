from abc import abstractmethod
import inspect
from typing import Any, Generic, Protocol
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class ProcessorInterface(
    Generic[TPayload],
    Protocol,
):
    @abstractmethod
    async def process(
        self,
        stages: list[PipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        pass

    async def _call_stage(
        self,
        stage: PipelineCallable[TPayload],
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        result = stage(payload)

        if inspect.isawaitable(result):
            return await result

        return result
