# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.24.0"

# Re-exporting symbols
from _api import ChainedPipeline as ChainedPipeline
from _api import ChainedProcessor as ChainedProcessor
from _api import InterruptiblePipeline as InterruptiblePipeline
from _api import InterruptibleProcessor as InterruptibleProcessor
from _api import Pipeline as Pipeline
from _api import PipelineFactory as PipelineFactory
from _api import PipelineFactoryInterface as PipelineFactoryInterface
from _api import PipelineInterface as PipelineInterface
from _api import Processor as Processor
from _api import ProcessorInterface as ProcessorInterface
from _api import Stage as Stage
from _api import StageCallable as StageCallable
from _api import StageClassOrInstance as StageClassOrInstance
from _api import StageCollection as StageCollection
from _api import StageInstance as StageInstance
from _api import StageInstanceCollection as StageInstanceCollection
from _api import StageInterface as StageInterface
from _api import T_in as T_in
from _api import T_out as T_out
from _api import __all__ as _api_all

# pyright: reportUnsupportedDunderAll=false
__all__ = (*_api_all,)
