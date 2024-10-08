from typing import Protocol, Self

from ..with_base.stage_callable import StageCallable
from ..with_base.payload_type import TPayload
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..with_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)


class PipelineInterfaceMixin(
    WithPipelineProcessorInterface[TPayload],
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    def pipe(self, stage: StageCallable[TPayload]) -> Self: ...
