from thecodecrate_pipeline import (
    ProcessorInterface,
    PipelineItem,
)


class StubProcessor(ProcessorInterface[int]):
    async def process(
        self,
        stages: list[PipelineItem[int, ...]],
        payload: int,
    ) -> int:
        for stage in stages:
            payload = await self._call_stage(payload, stage)

        return payload * 10
