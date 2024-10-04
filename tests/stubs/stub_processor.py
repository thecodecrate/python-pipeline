from thecodecrate_pipeline import (
    Processor,
    PipelineItem,
)


class StubProcessor(Processor[int]):
    async def process(
        self,
        stages: list[PipelineItem[int, ...]],
        payload: int,
    ) -> int:
        for stage in stages:
            payload = await self._call_stage(payload, stage)

        return payload * 10
