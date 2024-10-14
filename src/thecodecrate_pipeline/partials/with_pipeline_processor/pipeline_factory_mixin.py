from abc import ABC
from typing import Any, Optional, Self

from .processor_interface import ProcessorInterface
from .pipeline_factory_interface_mixin import (
    PipelineFactoryInterfaceMixin as PipelineFactoryInterface,
)


class PipelineFactoryMixin(
    PipelineFactoryInterface,
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

        if not self.processor_class:
            self.processor_class = processor_class or None

        if not self.processor:
            self.processor = processor or None

    def with_processor(self, processor: ProcessorInterface) -> Self:
        self.processor = processor

        return self

    def with_processor_class(
        self, processor_class: type[ProcessorInterface]
    ) -> Self:
        self.processor_class = processor_class

        return self

    # ActAsFactory
    def _definition(self) -> dict[str, Any]:
        return {
            **super()._definition(),  # type: ignore
            "processor_class": self.processor_class,
            "processor": self.processor,
        }
