from abc import abstractmethod
from typing import Awaitable, Callable, Concatenate

from thecodecrate_pipeline import (
    Pipeline,
    Processor,
    Stage,
    TPayload,
)


class IndexedStage(Stage[TPayload]):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        tag: int,
    ) -> TPayload:
        pass


IndexedPipelineCallable = (
    IndexedStage[TPayload]
    | Callable[Concatenate[TPayload, ...], Awaitable[TPayload]]
    | Callable[Concatenate[TPayload, ...], TPayload]
)


class IndexedProcessor(Processor[TPayload]):
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
