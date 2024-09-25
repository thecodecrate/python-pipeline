from typing import Generic
from ...core.pipeline.payload import TPayload
from ...traits.with_processor.processor_interface import ProcessorInterface
from ...traits.with_stages.stage_interface import StageOrCallable


class ChainedProcessor(
    ProcessorInterface[TPayload],
    Generic[TPayload],
):
    def process(
        self,
        stages: list[StageOrCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        for stage in stages:
            payload = stage(payload)

        return payload
