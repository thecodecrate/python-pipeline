from typing import Generic

from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload
from ...traits.with_processor.processor_interface import ProcessorInterface


class ChainedProcessor(
    ProcessorInterface[TPayload],
    Generic[TPayload],
):
    async def process(
        self,
        stages: list[PipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(stage, payload)

        return payload
