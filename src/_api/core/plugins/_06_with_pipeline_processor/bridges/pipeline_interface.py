from typing import Protocol, TypeVar

# extends: outside base
from ..._01_with_base import PipelineInterface as PipelineBaseInterface

# extends: outside mixins
from ..._02_with_pipeline_as_list import (
    PipelineInterfaceMixin as _02_WithPipelineAsListInterface,
)


class PipelineInterface(
    _02_WithPipelineAsListInterface,
    PipelineBaseInterface,
    Protocol,
):
    pass


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
