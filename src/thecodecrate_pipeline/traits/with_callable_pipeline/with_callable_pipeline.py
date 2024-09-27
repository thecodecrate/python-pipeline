from typing import Generic, Protocol
from ..with_builderable.with_builderable import WithBuilderable
from ..with_processor.with_processor import WithProcessor
from ..with_stages.with_stages import WithStages
from ..with_stages.stage_interface import StageInterface
from ...core.pipeline.payload import TPayload


class WithCallablePipeline(
    StageInterface[TPayload],
    WithProcessor[TPayload],
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    async def __call__(self, payload: TPayload) -> TPayload:
        return await self.process(payload)
