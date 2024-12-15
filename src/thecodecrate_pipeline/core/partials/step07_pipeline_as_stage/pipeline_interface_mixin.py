from typing import Protocol

from ..step01_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..step01_base.types import T_in, T_out
from ..step02_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..step06_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)
from .stage_facade import StageFacade as WithStageInterface


class PipelineInterfaceMixin(
    WithStageInterface[T_in, T_out],
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass
