from typing import Optional, Protocol, Self

from .pipelineable_facade import PipelineableFacade
from ..with_base.type_pipeline_callable import PipelineCallable
from ..with_base.type_payload import TPayload
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_pipeline_processor.processor_interface import ProcessorInterface


class PipelineInterfaceMixin(
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    def build(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> PipelineableFacade[TPayload]: ...

    def add(self, item: PipelineCallable[TPayload, ...]) -> Self: ...
