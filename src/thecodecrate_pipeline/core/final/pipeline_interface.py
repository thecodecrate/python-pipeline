from typing import Protocol

from ..partials.step01_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..partials.step01_base.types import T_in, T_out
from ..partials.step02_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..partials.step04_pipeline_declared_stages.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineDeclaredStagesInterface,
)
from ..partials.step06_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)
from ..partials.step07_pipeline_as_stage.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsStageInterface,
)


class PipelineInterface(
    WithPipelineAsStageInterface[T_in, T_out],
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineDeclaredStagesInterface,
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass
