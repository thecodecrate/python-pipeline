from typing import Protocol, TypeVar

# extends: outside base
from ..._01_with_base import PipelineInterface as PipelineBaseInterface


class PipelineInterface(
    PipelineBaseInterface,
    Protocol,
):
    pass


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
