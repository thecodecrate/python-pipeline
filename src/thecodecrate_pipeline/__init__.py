from .core.pipeline.pipeline import Pipeline
from .core.pipeline.pipeline_interface import PipelineInterface
from .traits.with_stages.stage_interface import StageInterface
from .traits.with_processor.processor_interface import ProcessorInterface
from .core.pipeline_builder.pipeline_builder import PipelineBuilder
from .core.pipeline_builder.pipeline_builder import PipelineBuilderInterface
from .core.pipeline.pipeline_callable import PipelineCallable
from .modules.processors.chained_processor import ChainedProcessor
from .modules.processors.interruptible_processor import InterruptibleProcessor
from .traits.with_callable_pipeline.with_callable_pipeline import (
    WithCallablePipeline,
)
from .traits.with_immutability.with_immutability import WithImmutability
from .traits.with_pipe.with_pipe import WithPipe
from .traits.with_pipeline_builder.with_pipeline_builder import (
    WithPipelineBuilder,
)
from .traits.with_processor.with_processor import WithProcessor
from .traits.with_stages.with_stages import WithStages

# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.1.0"

# Expose the public API
__all__ = [
    # Core
    "Pipeline",
    "PipelineInterface",
    "StageInterface",
    "ProcessorInterface",
    "PipelineBuilder",
    "PipelineBuilderInterface",
    "PipelineCallable",
    # Processors
    "ChainedProcessor",
    "InterruptibleProcessor",
    # Traits
    "WithCallablePipeline",
    "WithImmutability",
    "WithPipe",
    "WithPipelineBuilder",
    "WithProcessor",
    "WithStages",
]
