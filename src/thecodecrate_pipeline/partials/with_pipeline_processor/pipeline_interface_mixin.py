from abc import abstractmethod
from typing import Any, Protocol, Self

from .processor_interface import ProcessorInterface
from ..with_base.type_payload import TPayload
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    @abstractmethod
    async def process(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...

    def get_processor(
        self,
    ) -> ProcessorInterface[TPayload]: ...

    def set_processor(
        self,
        processor: ProcessorInterface[TPayload],
    ) -> Self: ...
