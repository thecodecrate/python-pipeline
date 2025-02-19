from typing import Any, Optional, Protocol, Self

from ..step01_base import Pipeline_Base_Interface, T_in, T_out
from ..step02_pipeline_as_list import Pipeline_WithPipelineAsList_Interface
from .processor_interface import ProcessorInterface


class PipelineInterfaceMixin(
    Pipeline_WithPipelineAsList_Interface,
    Pipeline_Base_Interface,
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

    def _make_processor(self) -> ProcessorInterface: ...

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out: ...
