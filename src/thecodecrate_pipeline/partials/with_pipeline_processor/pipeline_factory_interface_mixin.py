from typing import Any, Optional, Protocol, Self

from .processor_interface import ProcessorInterface
from ..with_base.types import T_in, T_out
from ..with_base.pipeline_interface import PipelineInterface
from ..with_pipeline_factory.pipeline_factory_interface import (
    PipelineFactoryInterface as WithPipelineFactoryBaseInterface,
)


class PipelineFactoryInterfaceMixin(
    WithPipelineFactoryBaseInterface[PipelineInterface],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        processor_class: Optional[type[ProcessorInterface]] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        processor: Optional[
            type[ProcessorInterface] | ProcessorInterface
        ] = None,
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
