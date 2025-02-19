from typing import Any, Optional, Protocol, Self

from ..step01_base import Pipeline_Base_Interface, T_in, T_out
from ..step05_pipeline_factory import PipelineFactory_Base_Interface
from .processor_interface import ProcessorInterface


class PipelineFactoryInterfaceMixin(
    PipelineFactory_Base_Interface[Pipeline_Base_Interface],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        processor_class: Optional[type[ProcessorInterface]] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        processor: Optional[type[ProcessorInterface] | ProcessorInterface] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self: ...

    def with_processor_instance(
        self, processor_instance: ProcessorInterface
    ) -> Self: ...

    def with_processor_class(
        self, processor_class: type[ProcessorInterface]
    ) -> Self: ...

    # ActAsFactory
    def _definition(self) -> dict[str, Any]: ...
