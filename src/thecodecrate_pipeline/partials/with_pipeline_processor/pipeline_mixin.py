from abc import ABC
from typing import Optional, Self

from .processor_interface import ProcessorInterface
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    PipelineInterface[T_in, T_out],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface[T_in, T_out]]] = None
    processor: Optional[ProcessorInterface[T_in, T_out]] = None

    async def process(
        self,
        payload: T_in,
    ) -> T_out:
        return await self.get_processor().process(
            payload=payload,
            stages=self.get_items(),
        )

    def get_processor(self) -> ProcessorInterface[T_in, T_out]:
        if self.processor:
            return self.processor

        if self.processor_class is None:
            raise ValueError("No processor set")

        if self.processor is None:
            self.processor = self.processor_class()

        return self.processor

    def set_processor(
        self, processor: ProcessorInterface[T_in, T_out]
    ) -> Self:
        self.processor = processor

        return self
