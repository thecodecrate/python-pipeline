from thecodecrate_pipeline import (
    ProcessorInterface,
    PipelineCallable,
)


class StubProcessor(ProcessorInterface[int]):
    def process(
        self,
        stages: list[PipelineCallable[int]],
        payload: int,
    ) -> int:
        for stage in stages:
            payload = stage(payload)

        return payload * 10
