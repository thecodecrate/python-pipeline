from abc import ABC
from typing import Any, Optional, Self

from ..step01_base import T_in, T_out
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsInterface,
)
from .processor_interface import ProcessorInterface


class PipelineMixin(
    ImplementsInterface[T_in, T_out],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface]]
    processor_instance: Optional[ProcessorInterface]

    def __init__(
        self,
        processor_class: Optional[type[ProcessorInterface]] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        processor: Optional[type[ProcessorInterface] | ProcessorInterface] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "processor_class"):
            self.processor_class = None

        if not hasattr(self, "processor_instance"):
            self.processor_instance = None

        if processor_class:
            self.processor_class = processor_class

        if processor_instance:
            self.processor_instance = processor_instance

        if processor:
            cloned = self.with_processor(processor)

            self.processor_class = cloned.processor_class

            self.processor_instance = cloned.processor_instance

        if not self.processor_instance:
            self.processor_instance = self._make_processor()

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self:
        """
        Attachs a processor (class or instance) to the pipeline.
        """
        if isinstance(processor, type):
            return self.with_processor_class(processor)

        return self.with_processor_instance(processor)

    def with_processor_instance(self, processor_instance: ProcessorInterface) -> Self:
        """
        Attachs a processor instance to the pipeline.
        """
        return self.clone(
            {
                "processor_class": processor_instance.__class__,
                "processor_instance": processor_instance,
            }
        )

    def with_processor_class(self, processor_class: type[ProcessorInterface]) -> Self:
        """
        Attachs a processor class to the pipeline.
        """
        return self.clone({"processor_class": processor_class})

    def _make_processor(self) -> ProcessorInterface:
        if self.processor_class is None:
            raise ValueError("Processor class not set")

        return self.processor_class()

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out:
        """
        Process the given payload through the pipeline.
        """
        if self.processor_instance is None:
            raise ValueError("Processor not set")

        return await self.processor_instance.process(
            payload=payload, stages=self._get_items(), *args, **kwds
        )
