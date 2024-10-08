import inspect
from typing import Any

from ..partials.with_base.stage_callable import StageCallable
from ..partials.with_base.payload_type import TPayload
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
    check: StageCallable[TPayload]

    def __init__(
        self,
        check: StageCallable[TPayload],
    ) -> None:
        self.check = check

    async def process(
        self,
        payload: TPayload,
        stages: list[StageCallable[TPayload]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        for stage in stages:
            payload = await self._call_stage(payload, stage, *args, **kwds)

            if not await self._call_check(payload):
                return payload

        return payload

    async def _call_check(self, payload: TPayload) -> TPayload:
        result = self.check(payload)

        if inspect.isawaitable(result):
            return await result

        return result
