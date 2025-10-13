"""A collection of processors and their pipelines"""

# Re-exporting symbols
from _lib.processors.chained_processor.chained_pipeline import (
    ChainedPipeline as ChainedPipeline,
)
from _lib.processors.chained_processor.chained_processor import (
    ChainedProcessor as ChainedProcessor,
)
from _lib.processors.interruptible_processor.interruptible_pipeline import (
    InterruptiblePipeline as InterruptiblePipeline,
)
from _lib.processors.interruptible_processor.interruptible_processor import (
    InterruptibleProcessor as InterruptibleProcessor,
)

__all__ = (
    "ChainedPipeline",
    "ChainedProcessor",
    "InterruptiblePipeline",
    "InterruptibleProcessor",
)
