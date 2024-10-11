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
    processor_class: Optional[type[ProcessorInterface[T_in, T_out]]] = None
    processor: Optional[ProcessorInterface[T_in, T_out]] = None

    def __init__(
        self,
        processor: Optional[ProcessorInterface[T_in, T_out]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        self.processor = processor or self._make_processor()

    def _make_processor(self) -> ProcessorInterface[T_in, T_out]:
        if self.processor_class is None:
            raise ValueError("Processor class not set")

        return self.processor_class()

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out:
        if self.processor is None:
            raise ValueError("Processor not set")

        return await self.processor.process(
            payload=payload, stages=self.get_items(), *args, **kwds
        )
