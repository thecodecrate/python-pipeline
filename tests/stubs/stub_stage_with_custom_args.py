from abc import abstractmethod
from typing import Awaitable, Callable, Concatenate

from thecodecrate_pipeline import (
    PipelineInterface,
    ProcessorInterface,
    StageInterface,
)
from thecodecrate_pipeline.core.pipeline.payload import TPayload


class IndexedStageInterface(StageInterface[TPayload]):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        tag: int,
    ) -> TPayload:
        pass


IndexedPipelineCallable = (
    IndexedStageInterface[TPayload]
    | Callable[Concatenate[TPayload, ...], Awaitable[TPayload]]
    | Callable[Concatenate[TPayload, ...], TPayload]
)


class IndexedProcessor(ProcessorInterface[TPayload]):
    async def process(
        self,
        stages: list[IndexedPipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        index = 0

        for stage in stages:
            payload = await self._call_stage(
                stage=stage,
                payload=payload,
                index=index,
            )

            index += 1

        return payload


class IndexedPipeline(PipelineInterface[TPayload]):
    processor_class = IndexedProcessor
