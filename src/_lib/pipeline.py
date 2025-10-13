from typing import TypeVar

from .concerns.base_pipeline import BasePipeline
from .concerns.processable_pipeline import ProcessablePipeline
from .concerns.stageable_pipeline import StageablePipeline
from .contracts.pipeline import Pipeline as ImplementsInterface
from .types.types import T_in, T_out


class Pipeline(
    ProcessablePipeline[T_in, T_out],
    StageablePipeline[T_in, T_out],
    BasePipeline[T_in, T_out],
    ImplementsInterface[T_in, T_out],
):
    pass


TPipeline = TypeVar("TPipeline", bound=Pipeline, infer_variance=True)
