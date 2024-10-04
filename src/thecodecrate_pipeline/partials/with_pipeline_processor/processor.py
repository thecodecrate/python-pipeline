from abc import abstractmethod
import inspect
from typing import Any

from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_callable import PipelineCallable


class Processor(
    ImplementsProcessorInterface[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineCallable[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass

    async def _call_stage(
        self,
        payload: TPayload,
        stage: PipelineCallable[TPayload, ...],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        result = stage(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
