from ...classes.pipeline import Pipeline
from ...classes.types import T_in, T_out
from .chained_processor import ChainedProcessor


class ChainedPipeline(Pipeline[T_in, T_out]):
    processor_class = ChainedProcessor
