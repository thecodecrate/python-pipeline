from typing import Any, Generic

from ..partials.with_base.type_pipeline_callable import PipelineCallable
from ..partials.with_base.type_payload import TPayload
from ..partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorConcern,
)


class ChainedProcessor(
    WithProcessorConcern[TPayload],
    ImplementsProcessorInterface[TPayload],
    Generic[TPayload],
):
    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineCallable[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(payload, stage, *args, **kwds)

        return payload
