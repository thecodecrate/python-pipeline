from thecodecrate_pipeline import (
    ProcessorInterface,
    PipelineCallable,
)


class StubProcessor(ProcessorInterface[int]):
    async def process(
        self,
        stages: list[PipelineCallable[int, ...]],
        payload: int,
    ) -> int:
        for stage in stages:
            payload = await self._call_stage(stage, payload)

        return payload * 10
