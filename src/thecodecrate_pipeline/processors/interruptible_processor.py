from typing import Any, Generic

from ..partials.with_base.type_pipeline_item import PipelineItem
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
    Generic[TPayload],
):
    check: PipelineItem[TPayload, ...]

    def __init__(
        self,
        check: PipelineItem[TPayload, ...],
    ) -> None:
        self.check = check

    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineItem[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(payload, stage, *args, **kwds)

            if not self.check(payload):
                return payload

        return payload
