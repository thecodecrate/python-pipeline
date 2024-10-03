from typing import Optional, Protocol, Self

from .processor_interface import ProcessorInterface
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as PipelineInterface,
)
from ..with_base.type_payload import TPayload


class PipelineMixin(
    PipelineInterface[TPayload],
    Protocol[TPayload],
):
    processor_class: Optional[type[ProcessorInterface[TPayload]]] = None

    processor: Optional[ProcessorInterface[TPayload]] = None

    async def process(
        self,
        payload: TPayload,
    ) -> TPayload:
        return await self.get_processor().process(
            payload=payload,
            stages=self.get_items(),
        )

    def get_processor(self) -> ProcessorInterface[TPayload]:
        if self.processor:
            return self.processor

        if self.processor_class is None:
            raise ValueError("No processor set")

        if self.processor is None:
            self.processor = self.processor_class()

        return self.processor

    def set_processor(self, processor: ProcessorInterface[TPayload]) -> Self:
        self.processor = processor

        return self
