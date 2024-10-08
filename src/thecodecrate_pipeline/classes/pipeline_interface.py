from typing import Protocol

from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..partials.with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..partials.with_pipeline_declared_stages.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineDeclaredStagesInterface,
)
from ..partials.with_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)
from ..partials.with_pipeline_as_stage.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsStageInterface,
)
from ..partials.with_pipeline_as_immutable.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsImmutableInterface,
)
from ..partials.with_pipelineable_methods.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineableMethodsInterface,
)


class PipelineInterface(
    WithPipelineableMethodsInterface[T_in, T_out],
    WithPipelineAsImmutableInterface,
    WithPipelineAsStageInterface[T_in, T_out],
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineDeclaredStagesInterface,
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass
