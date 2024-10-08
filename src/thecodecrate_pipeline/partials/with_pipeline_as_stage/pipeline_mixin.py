from abc import ABC
from typing import Any

from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    ImplementsPipelineInterface[T_in, T_out],
    ABC,
):
    async def __call__(
        self,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await self.process(payload, *args, **kwds)
