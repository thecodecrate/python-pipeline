"""A collection of processors and their pipelines"""

# Re-exporting symbols
from _api.processors import ChainedPipeline as ChainedPipeline
from _api.processors import ChainedProcessor as ChainedProcessor
from _api.processors import InterruptiblePipeline as InterruptiblePipeline
from _api.processors import InterruptibleProcessor as InterruptibleProcessor
from _api.processors import __all__ as _processors_all

# pyright: reportUnsupportedDunderAll=false
__all__ = (*_processors_all,)
