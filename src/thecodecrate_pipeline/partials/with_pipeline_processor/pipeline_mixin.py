from abc import ABC
from typing import Any, Optional, Self

from .processor_interface import ProcessorInterface
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    PipelineInterface[T_in, T_out],
    ABC,
):
    base_processor_class: type[ProcessorInterface[T_in, T_out]] | None = None
    processor_class: Optional[type[ProcessorInterface[T_in, T_out]]] = None
    processor: Optional[ProcessorInterface[T_in, T_out]] = None

    async def process(
        self,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await self.ensure_processor().process(
            payload=payload,
            stages=self.get_items(),
            *args,
            **kwds,
        )

    def make_processor(self) -> ProcessorInterface[T_in, T_out]:
        if self.processor_class is None:
            raise ValueError("Processor class not set")

        return self.processor_class()

    def ensure_processor(self) -> ProcessorInterface[T_in, T_out]:
        if self.processor:
            return self.processor

        if self.processor is None:
            self.processor = self.make_processor()

        return self.processor

    def get_processor(self) -> ProcessorInterface[T_in, T_out] | None:
        return self.processor

    def set_processor(
        self, processor: ProcessorInterface[T_in, T_out]
    ) -> Self:
        self.processor = processor

        return self

    def get_base_processor_class(
        self,
    ) -> type[ProcessorInterface[T_in, T_out]]:
        if self.base_processor_class is None:
            raise ValueError("Base processor class not set")

        return self.base_processor_class
