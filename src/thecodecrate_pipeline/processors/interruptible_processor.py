from typing import Any

from ..partials.with_base.type_pipeline_callable import PipelineCallable
from ..partials.with_base.type_payload import TPayload
from ..partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorConcern,
)


class InterruptibleProcessor(
    WithProcessorConcern[TPayload],
    ImplementsProcessorInterface[TPayload],
):
    check: PipelineCallable[TPayload, ...]

    def __init__(
        self,
        check: PipelineCallable[TPayload, ...],
    ) -> None:
        self.check = check

    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineCallable[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(payload, stage, *args, **kwds)

            if not self.check(payload):
                return payload

        return payload
