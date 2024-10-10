from ...classes.pipeline import Pipeline
from ...classes.types import T_in, T_out
from .stateful_chained_processor import StatefulChainedProcessor


class StatefulChainedPipeline(Pipeline[T_in, T_out]):
    processor_class = StatefulChainedProcessor
