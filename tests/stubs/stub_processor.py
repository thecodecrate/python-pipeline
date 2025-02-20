from thecodecrate_pipeline import (
    Processor,
    StageInstanceCollection,
)


class StubProcessor(Processor[int]):
    async def process(
        self,
        payload: int,
        stages: StageInstanceCollection,
    ) -> int:
        for stage in stages:
            payload = await self._call(callable=stage, payload=payload)

        return payload * 10
