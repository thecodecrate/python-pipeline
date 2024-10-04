from abc import abstractmethod
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
    ) -> TPayload: ...

    async def _call_stage(
        self,
        payload: TPayload,
        stage: PipelineItem[TPayload, ...],
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...
