# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.28.0"

# Re-exporting symbols
from _lib.contracts.pipeline import Pipeline as PipelineInterface
from _lib.contracts.pipeline_factory import PipelineFactory as PipelineFactoryInterface
from _lib.contracts.processor import Processor as ProcessorInterface
from _lib.contracts.stage import Stage as StageInterface
from _lib.pipeline import Pipeline as Pipeline
from _lib.pipeline_factory import PipelineFactory as PipelineFactory
from _lib.processor import Processor as Processor
from _lib.stage import Stage as Stage

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
