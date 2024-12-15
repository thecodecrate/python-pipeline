from ...core.final.pipeline import Pipeline
from ...core.final.types import T_in, T_out
from .chained_processor import ChainedProcessor


class ChainedPipeline(Pipeline[T_in, T_out]):
    processor_class = ChainedProcessor
