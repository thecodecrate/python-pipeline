from typing import Protocol, TypeVar

# extends: outside base
from ..._01_with_base import PipelineInterface as PipelineBaseInterface

# extends: outside mixins
from ..._02_with_pipeline_as_list import (
    PipelineInterfaceMixin as _02_WithPipelineAsListInterface,
)
from ..._04_with_pipeline_declared_stages import (
    PipelineInterfaceMixin as _04_WithPipelineDeclaredStagesInterface,
)
from ..._06_with_pipeline_processor import (
    PipelineInterfaceMixin as _06_WithPipelineProcessorInterface,
)
from ..._08_with_pipeline_as_stage import (
    PipelineInterfaceMixin as _08_WithPipelineAsStageInterface,
)

# uses: bridge interface
from .types import T_in, T_out


class PipelineInterface(
    _08_WithPipelineAsStageInterface[T_in, T_out],
    _06_WithPipelineProcessorInterface[T_in, T_out],
    _04_WithPipelineDeclaredStagesInterface,
    _02_WithPipelineAsListInterface,
    PipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
