from typing import Any, Protocol, TypeVar

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


class PipelineableFacade(
    WithPipelineProcessorInterface[T_in, T_out],
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass


TPipelineable = TypeVar("TPipelineable", bound=PipelineableFacade[Any, Any])
