# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.26.0"

# Re-exporting symbols
from .pipeline import CallableCollection as CallableCollection
from .pipeline import CallableType as CallableType
from .pipeline import Pipeline as Pipeline
from .pipeline import PipelineFactory as PipelineFactory
from .pipeline import PipelineFactoryInterface as PipelineFactoryInterface
from .pipeline import PipelineInterface as PipelineInterface
from .pipeline import Processor as Processor
from .pipeline import ProcessorInterface as ProcessorInterface
from .pipeline import Stage as Stage
from .pipeline import StageDefinition as StageDefinition
from .pipeline import StageDefinitionCollection as StageDefinitionCollection
from .pipeline import StageInterface as StageInterface
from .pipeline import T_in as T_in
from .pipeline import T_out as T_out
from .pipeline import __all__ as _pipeline_all
from .processors import ChainedPipeline as ChainedPipeline
from .processors import ChainedProcessor as ChainedProcessor
from .processors import InterruptiblePipeline as InterruptiblePipeline
from .processors import InterruptibleProcessor as InterruptibleProcessor
from .processors import __all__ as _processor_all

# pyright: reportUnsupportedDunderAll=false
__all__ = (
    *_pipeline_all,
    *_processor_all,
)
