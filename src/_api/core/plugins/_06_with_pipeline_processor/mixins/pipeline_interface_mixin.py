from typing import Any, Optional, Protocol, Self

# extends: self-bridge
from .._bridges.pipeline_interface import PipelineInterface

# uses: bridge interface
from .._bridges.types import T_in, T_out

# uses: local base
from ..bases.processor_interface import ProcessorInterface


class PipelineInterfaceMixin(
    PipelineInterface,
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

    def get_processor_instance(self) -> Optional[ProcessorInterface]: ...

    def get_processor_class(self) -> Optional[type[ProcessorInterface]]: ...

    def _get_default_processor_class(self) -> Optional[type[ProcessorInterface]]: ...
