from typing import Any

from ...core import Pipeline, T_in, T_out
from .interruptible_processor import CheckCallable, InterruptibleProcessor


class InterruptiblePipeline(Pipeline[T_in, T_out]):
    """Pipeline with conditional interruption."""

    def __init__(self, check: CheckCallable, *args: Any, **kwargs: Any):
        """Constructor.

        Parameters:
            check: Callable used to interrupt processing.

        Example:
            ```python
            # Interrupts when payload value exceeds 100
            pipeline = (
                InterruptiblePipeline[int](lambda payload: payload > 100)
                .pipe(lambda payload: payload + 2)
                .pipe(lambda payload: payload * 10)
                .pipe(lambda payload: payload * 10)
            )

            # Process payload - will stop if value exceeds 100
            assert await pipeline.process(5) == 70
            ```
        """
        processor = InterruptibleProcessor[T_in, T_out](check)

        super().__init__(processor=processor, *args, **kwargs)
