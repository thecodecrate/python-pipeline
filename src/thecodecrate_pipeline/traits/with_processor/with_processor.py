from typing import Generic, Optional, Protocol, Self
from .processor_interface import ProcessorInterface
from ..with_builderable.with_builderable import WithBuilderable
from ..with_stages.with_stages import WithStages
from ...core.pipeline.payload import TPayload


class WithProcessor(
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    processor_class: Optional[type[ProcessorInterface[TPayload]]] = None

    processor: Optional[ProcessorInterface[TPayload]] = None

    async def process(
        self,
        payload: TPayload,
    ) -> TPayload:
        return await self.get_processor().process(self.get_parts(), payload)

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
