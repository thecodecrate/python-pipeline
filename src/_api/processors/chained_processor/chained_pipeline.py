from typing import Any

from ...core import Pipeline, T_in, T_out
from .chained_processor import ChainedProcessor


class ChainedPipeline(Pipeline[T_in, T_out]):
    """Default pipeline (`Pipeline` alias). Sequentially processes data through multiple stages."""

    def __init__(self, *args: Any, **kwargs: Any):
        """Constructor.

        Example:
            ```python
            # Process data through multiple stages
            pipeline = (
                (ChainedPipeline[int]())
                .pipe(lambda payload: payload + 1)
                .pipe(lambda payload: payload * 2)
                .pipe(lambda payload: payload + 1)
            )

            # Assert result
            assert await pipeline.process(1) == 5
            ```
        """
        processor = ChainedProcessor[T_in, T_out]()

        super().__init__(processor=processor, *args, **kwargs)
