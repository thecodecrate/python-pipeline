# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.23.0"

# Re-exporting symbols
from .core import Pipeline as Pipeline
from .core import PipelineFactory as PipelineFactory
from .core import PipelineFactoryInterface as PipelineFactoryInterface
from .core import PipelineInterface as PipelineInterface
from .core import Processor as Processor
from .core import ProcessorInterface as ProcessorInterface
from .core import Stage as Stage
from .core import StageCallable as StageCallable
from .core import StageClassOrInstance as StageClassOrInstance
from .core import StageCollection as StageCollection
from .core import StageInstance as StageInstance
from .core import StageInstanceCollection as StageInstanceCollection
from .core import StageInterface as StageInterface
from .core import T_in as T_in
from .core import T_out as T_out
from .core import __all__ as _core_all
from .processors import ChainedPipeline as ChainedPipeline
from .processors import ChainedProcessor as ChainedProcessor
from .processors import InterruptiblePipeline as InterruptiblePipeline
from .processors import InterruptibleProcessor as InterruptibleProcessor
from .processors import __all__ as _processor_all

# pyright: reportUnsupportedDunderAll=false
__all__ = (
    *_core_all,
    *_processor_all,
)
