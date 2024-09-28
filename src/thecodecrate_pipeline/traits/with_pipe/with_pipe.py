from typing import Protocol, Self

from ..with_builderable.with_builderable import WithBuilderable
from ..with_stages.with_stages import WithStages
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class WithPipe(
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Protocol[TPayload],
):
    def pipe(self, stage: PipelineCallable[TPayload, ...]) -> Self:
        return self.add_part(stage)
