from abc import ABC
from typing import Any, Generic, Optional, cast

from .processor_interface_mixin import (
    ProcessorInterfaceMixin as ProcessorInterface,
)
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    ImplementsPipelineInterface[T_in, T_out],
    Generic[T_in, T_out],
    ABC,
):
    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out:
        self.processor_instance = cast(
            Optional[ProcessorInterface], self.processor_instance
        )  # type: ignore

        if self.processor_instance is None:
            raise ValueError("Processor not set")

        return await self.processor_instance.process_with_strategy(
            payload=payload, stages=self._get_items(), *args, **kwds
        )
