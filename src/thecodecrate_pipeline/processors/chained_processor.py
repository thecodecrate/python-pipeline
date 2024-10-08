from typing import Any

from ..partials.with_base.stage_callable import StageCallable
from ..partials.with_base.payload_type import TPayload
from ..partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorConcern,
)


class ChainedProcessor(
    WithProcessorConcern[TPayload],
    ImplementsProcessorInterface[TPayload],
):
    async def process(
        self,
        payload: TPayload,
        stages: list[StageCallable[TPayload]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(payload, stage, *args, **kwds)

        return payload
