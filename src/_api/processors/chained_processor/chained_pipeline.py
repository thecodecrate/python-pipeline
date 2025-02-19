from ...core import Pipeline, T_in, T_out
from .chained_processor import ChainedProcessor


class ChainedPipeline(Pipeline[T_in, T_out]):
    processor_class = ChainedProcessor
