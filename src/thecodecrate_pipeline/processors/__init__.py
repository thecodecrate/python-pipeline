"""A collection of processors and their pipelines"""

# Re-exporting symbols
from _lib.processors import ChainedPipeline as ChainedPipeline
from _lib.processors import ChainedProcessor as ChainedProcessor
from _lib.processors import InterruptiblePipeline as InterruptiblePipeline
from _lib.processors import InterruptibleProcessor as InterruptibleProcessor
from _lib.processors import __all__ as _processors_all

# pyright: reportUnsupportedDunderAll=false
__all__ = (*_processors_all,)
