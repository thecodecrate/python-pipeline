from abc import ABC
from typing import Any, Optional, Self

from ..with_base.types import T_in, T_out
from .processor_interface import ProcessorInterface
from .pipeline_factory_interface_mixin import (
    PipelineFactoryInterfaceMixin as PipelineFactoryInterface,
)


class PipelineFactoryMixin(
    PipelineFactoryInterface[T_in, T_out],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface[T_in, T_out]]] = None
    processor_instance: Optional[ProcessorInterface[T_in, T_out]] = None

    def __init__(
        self,
        processor_class: Optional[type[ProcessorInterface]] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        processor: Optional[
            type[ProcessorInterface] | ProcessorInterface
        ] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not self.processor_class:
            self.processor_class = processor_class or None

        if not self.processor_instance:
            self.processor_instance = processor_instance or None

        if processor:
            self.with_processor(processor)

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self:
        if isinstance(processor, type):
            return self.with_processor_class(processor)

        return self.with_processor_instance(processor)

    def with_processor_instance(
        self, processor_instance: ProcessorInterface
    ) -> Self:
        self.processor_class = processor_instance.__class__

        self.processor_instance = processor_instance

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
            "processor_instance": self.processor_instance,
        }
