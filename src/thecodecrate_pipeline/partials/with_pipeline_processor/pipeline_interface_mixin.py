from abc import abstractmethod
from typing import Any, Protocol, Self

from .processor_interface import ProcessorInterface
from ..with_base.types import T_in, T_out
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    def get_processor(
        self,
    ) -> ProcessorInterface[T_in, T_out]: ...

    def set_processor(
        self,
        processor: ProcessorInterface[T_in, T_out],
    ) -> Self: ...
