from thecodecrate_pipeline import (
    Processor,
    PipelineCallable,
)


class StubProcessor(Processor[int]):
    async def process(
        self,
        stages: list[PipelineCallable[int, ...]],
        payload: int,
    ) -> int:
        for stage in stages:
            payload = await self._call_stage(payload, stage)

        return payload * 10
