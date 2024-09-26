from abc import ABC
from typing import Generic, Optional, cast

from .parent_class import TParentClass
from .processor_interface import ProcessorInterface
from ...core.pipeline.payload import TPayload


class WithProcessor(
    Generic[TParentClass, TPayload],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface[TPayload]]] = None
    processor: Optional[ProcessorInterface[TPayload]] = None

    def process(
        self,
        payload: TPayload,
    ) -> TPayload:
        this = cast(TParentClass, self)

        return self.get_processor().process(this.stages, payload)

    def get_processor(self) -> ProcessorInterface[TPayload]:
        if self.processor:
            return self.processor

        if self.processor_class is None:
            raise ValueError("No processor set")

        if self.processor is None:
            self.processor = self.processor_class()

        return self.processor

    def build_parts(
        self,
        payload: TPayload,
    ) -> TPayload:
        return self.process(payload)
