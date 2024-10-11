from typing import Any

from ...classes.pipeline import Pipeline
from ...classes.types import T_in, T_out
from .interruptible_processor import InterruptibleProcessor, CheckCallable


class InterruptiblePipeline(Pipeline[T_in, T_out]):
    def __init__(self, check: CheckCallable, *args: Any, **kwargs: Any):
        processor = InterruptibleProcessor[T_in, T_out](check)

        super().__init__(processor=processor, *args, **kwargs)
