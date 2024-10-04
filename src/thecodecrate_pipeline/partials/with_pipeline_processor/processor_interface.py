from abc import abstractmethod
from typing import Any, Protocol

from ..with_base.type_payload import TPayload
from ..with_base.type_pipeline_callable import PipelineCallable


class ProcessorInterface(
    Protocol[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        stages: list[PipelineCallable[TPayload, ...]],
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...

    async def _call_stage(
        self,
        payload: TPayload,
        stage: PipelineCallable[TPayload, ...],
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...
