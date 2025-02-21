from ...core import ChainedProcessor as ChainedProcessorBase
from ...core import T_in, T_out


class ChainedProcessor(ChainedProcessorBase[T_in, T_out]):
    """Default processor. Sequentially processes data through multiple stages.

    Example:
        ```python
        # Create processor
        processor = ChainedProcessor[int]()

        # Stages
        result = await processor.process(
            payload=5,
            stages=(
                lambda payload: payload + 1,
                lambda payload: payload * 2,
            ),
        )

        # Assert result
        assert result == 12
        ```
    """
