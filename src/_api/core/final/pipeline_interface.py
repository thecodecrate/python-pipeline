from typing import Protocol, TypeVar

# extends: outside base
from ..plugins._01_with_base import PipelineInterface as PipelineBaseInterface

# extends: outside mixins
from ..plugins._02_with_pipeline_as_list import (
    PipelineInterfaceMixin as _02_WithPipelineAsListInterface,
)
from ..plugins._04_with_pipeline_declared_stages import (
    PipelineInterfaceMixin as _04_WithPipelineDeclaredStagesInterface,
)
from ..plugins._06_with_pipeline_processor import (
    PipelineInterfaceMixin as _06_WithPipelineProcessorInterface,
)
from ..plugins._08_with_pipeline_as_stage import (
    PipelineInterfaceMixin as _08_WithPipelineAsStageInterface,
)
from ..plugins._99_with_pipeline_default_processor import (
    PipelineInterfaceMixin as _99_WithPipelineDefaultProcessorInterface,
)

# uses: bridge interface
from .types import T_in, T_out


class PipelineInterface(
    _99_WithPipelineDefaultProcessorInterface[T_in, T_out],
    _08_WithPipelineAsStageInterface[T_in, T_out],
    _06_WithPipelineProcessorInterface[T_in, T_out],
    _04_WithPipelineDeclaredStagesInterface,
    _02_WithPipelineAsListInterface,
    PipelineBaseInterface,
    Protocol[T_in, T_out],
):
    pass


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
