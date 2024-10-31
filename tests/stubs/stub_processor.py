from thecodecrate_pipeline import (
    Processor,
    StageInstanceCollection,
)


class StubProcessor(Processor[int]):
    async def process(
        self,
        stages: StageInstanceCollection,
        payload: int,
    ) -> int:
        for stage in stages:
            payload = await self._call(stage=stage, payload=payload)

        return payload * 10
