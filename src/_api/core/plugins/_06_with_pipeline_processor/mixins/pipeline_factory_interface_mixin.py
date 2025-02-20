from typing import Any, Optional, Protocol, Self

# uses: local base
from ..bases.processor_interface import ProcessorInterface

# extends: self-bridge
from ..bridges.pipeline_factory_interface import PipelineFactoryInterface

# uses: bridge interface
from ..bridges.types import T_in, T_out


class PipelineFactoryInterfaceMixin(
    PipelineFactoryInterface[T_in, T_out],
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
