from abc import abstractmethod
import inspect
from typing import Any, Protocol

from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_item import PipelineItem


class ProcessorInterface(
    Protocol[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineItem[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass

    async def _call_stage(
        self,
        payload: TPayload,
        stage: PipelineItem[TPayload, ...],
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        result = stage(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
