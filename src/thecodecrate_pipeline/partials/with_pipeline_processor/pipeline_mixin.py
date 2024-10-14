from abc import ABC
from typing import Any, Optional

from .processor_interface import ProcessorInterface
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)
from ..with_base.types import T_in, T_out


class PipelineMixin(
    PipelineInterface[T_in, T_out],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface]] = None
    processor: Optional[ProcessorInterface] = None

    def __init__(
        self,
        processor_class: Optional[type[ProcessorInterface]] = None,
        processor: Optional[ProcessorInterface] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if processor_class:
            self.processor_class = processor_class

        if processor:
            self.processor = processor

        if not self.processor:
            self.processor = self._make_processor()

    def _make_processor(self) -> ProcessorInterface:
        if self.processor_class is None:
            raise ValueError("Processor class not set")

        return self.processor_class()

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out:
        if self.processor is None:
            raise ValueError("Processor not set")

        return await self.processor.process(
            payload=payload, stages=self._get_items(), *args, **kwds
        )
