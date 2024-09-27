from typing import Generic, Protocol, Self
from ..with_builderable.with_builderable import WithBuilderable
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload


class WithStages(
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    stages: list[PipelineCallable[TPayload]] = []

    def get_parts(self) -> list[PipelineCallable[TPayload]]:
        return self.stages

    def set_parts(self, parts: list[PipelineCallable[TPayload]]) -> Self:
        self.stages = parts

        return self
