# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.26.0"

# Re-exporting symbols
from _api.core import Pipeline as Pipeline
from _api.core import PipelineFactory as PipelineFactory
from _api.core import PipelineFactoryInterface as PipelineFactoryInterface
from _api.core import PipelineInterface as PipelineInterface
from _api.core import Processor as Processor
from _api.core import ProcessorInterface as ProcessorInterface
from _api.core import Stage as Stage
from _api.core import StageCallable as StageCallable
from _api.core import StageInterface as StageInterface

# pyright: reportUnsupportedDunderAll=false
__all__ = (
    "Pipeline",
    "PipelineFactory",
    "PipelineFactoryInterface",
    "PipelineInterface",
    "Processor",
    "ProcessorInterface",
    "Stage",
    "StageCallable",
    "StageInterface",
)
