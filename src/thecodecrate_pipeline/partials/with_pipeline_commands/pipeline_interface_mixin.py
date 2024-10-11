from typing import Protocol

from .command_facade import TCommand
from .processor_facade import ProcessorFacade
from ..with_base.types import T_in, T_out
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
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[TCommand, T_in, T_out],
):
    def _should_make_command_processor(self) -> bool: ...

    def _make_command_processor(self) -> ProcessorFacade: ...
