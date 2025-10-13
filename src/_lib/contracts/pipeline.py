from typing import Protocol

from ..types.types import T_in, T_out
from .base_pipeline import BasePipeline as BasePipelineContract
from .processable_pipeline import ProcessablePipeline as ProcessablePipelineContract
from .stageable_pipeline import StageablePipeline as StageablePipelineContract


class Pipeline(
    ProcessablePipelineContract[T_in, T_out],
    StageablePipelineContract[T_in, T_out],
    BasePipelineContract[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
