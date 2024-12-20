from typing import Any, Optional, Protocol, Self

from ..step01_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..step01_base.types import T_in, T_out
from ..step02_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from .processor_interface import ProcessorInterface


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
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
