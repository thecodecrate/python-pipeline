from typing import Any, Protocol

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.type_payload import TPayload


class PipelineMixin(
    ImplementsPipelineInterface[TPayload],
    Protocol[TPayload],
):
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        return await self.process(payload, *args, **kwds)