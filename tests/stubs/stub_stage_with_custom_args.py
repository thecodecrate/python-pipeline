from abc import abstractmethod
from typing import Any, Awaitable, Callable, Concatenate, cast

from thecodecrate_pipeline import Pipeline, Processor, Stage
from thecodecrate_pipeline.types import CallableCollection, T_in, T_out


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
        stages: CallableCollection,
    ) -> T_out:
        index = 0

        payload_out: Any = payload

        for stage in stages:
            payload_out = await self._call(
                callable=stage, payload=payload_out, index=index
            )

            index += 1

        return cast(T_out, payload_out)


class IndexedPipeline(Pipeline[T_in]):
    processor = IndexedProcessor
