# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.27.0"

# Re-exporting symbols
from _lib import Pipeline as Pipeline
from _lib import PipelineFactory as PipelineFactory
from _lib import PipelineFactoryInterface as PipelineFactoryInterface
from _lib import PipelineInterface as PipelineInterface
from _lib import Processor as Processor
from _lib import ProcessorInterface as ProcessorInterface
from _lib import Stage as Stage
from _lib import StageInterface as StageInterface

# pyright: reportUnsupportedDunderAll=false
__all__ = (
    "Pipeline",
    "PipelineFactory",
    "PipelineFactoryInterface",
    "PipelineInterface",
    "Processor",
    "ProcessorInterface",
    "Stage",
    "StageInterface",
)
