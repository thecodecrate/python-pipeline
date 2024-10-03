from abc import abstractmethod
from typing import Awaitable, Callable, Concatenate

from thecodecrate_pipeline import (
    Pipeline,
    ProcessorInterface,
    StageInterface,
    TPayload,
)


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
        payload: TPayload,
        stages: list[IndexedPipelineCallable[TPayload]],
    ) -> TPayload:
        index = 0

        for stage in stages:
            payload = await self._call_stage(
                payload=payload,
                stage=stage,
                index=index,
            )

            index += 1

        return payload


class IndexedPipeline(Pipeline[TPayload]):
    processor_class = IndexedProcessor
