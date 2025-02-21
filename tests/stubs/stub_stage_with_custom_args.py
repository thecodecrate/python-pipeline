from abc import abstractmethod
from typing import Awaitable, Callable, Concatenate, cast

from thecodecrate_pipeline import Pipeline, Processor, Stage
from thecodecrate_pipeline.types import StageInstanceCollection, T_in, T_out


class IndexedStage(Stage[T_in, T_out]):
    @abstractmethod
    async def __call__(
        self,
        payload: T_in,
        /,
        tag: int,
    ) -> T_out:
        pass


IndexedPipelineCallable = (
    IndexedStage[T_in, T_out]
    | Callable[Concatenate[T_in, ...], Awaitable[T_out]]
    | Callable[Concatenate[T_in, ...], T_out]
)


class IndexedProcessor(Processor[T_in, T_out]):
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
    ) -> T_out:
        index = 0

        for stage in stages:
            payload = await self._call(callable=stage, payload=payload, index=index)

            index += 1

        return cast(T_out, payload)


class IndexedPipeline(Pipeline[T_in]):
    processor_class = IndexedProcessor
