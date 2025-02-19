from typing import Any

from ...core import Pipeline, T_in, T_out
from .interruptible_processor import CheckCallable, InterruptibleProcessor


class InterruptiblePipeline(Pipeline[T_in, T_out]):
    def __init__(self, check: CheckCallable, *args: Any, **kwargs: Any):
        processor = InterruptibleProcessor[T_in, T_out](check)

        super().__init__(processor=processor, *args, **kwargs)
