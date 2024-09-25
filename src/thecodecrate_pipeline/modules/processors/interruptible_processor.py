from typing import Generic

from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload
from ...traits.with_processor.processor_interface import ProcessorInterface


class InterruptibleProcessor(
    ProcessorInterface[TPayload],
    Generic[TPayload],
):
    check: PipelineCallable[TPayload]

    def __init__(
        self,
        check: PipelineCallable[TPayload],
    ) -> None:
        self.check = check

    def process(
        self,
        stages: list[PipelineCallable[TPayload]],
        payload: TPayload,
    ) -> TPayload:
        for stage in stages:
            payload = stage(payload)

            if not self.check(payload):
                return payload

        return payload
