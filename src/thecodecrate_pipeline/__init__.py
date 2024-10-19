from .classes.command import Command
from .classes.command_interface import CommandInterface
from .classes.pipeline_factory import PipelineFactory
from .classes.pipeline_factory_interface import PipelineFactoryInterface
from .classes.pipeline import Pipeline
from .classes.pipeline_interface import PipelineInterface
from .classes.processor import Processor
from .classes.processor_interface import ProcessorInterface
from .classes.stage import Stage
from .classes.stage_interface import StageInterface
from .classes.types import T_in, T_out
from .processors.chained_processor.chained_pipeline import ChainedPipeline
from .processors.chained_processor.chained_processor import ChainedProcessor
from .processors.interruptible_processor.interruptible_processor import (
    InterruptibleProcessor,
)
from .processors.interruptible_processor.interruptible_pipeline import (
    InterruptiblePipeline,
)
from .partials.with_base.stage_callable import StageCallable
from .partials.with_base.pipeline import Pipeline as WithPipelineBase
from .partials.with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from .partials.with_base.stage import Stage as WithStageBase
from .partials.with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from .partials.with_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsList,
)
from .partials.with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from .partials.with_pipeline_processor.pipeline_mixin import (
    PipelineMixin as WithPipelineProcessor,
)
from .partials.with_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)
from .partials.with_pipeline_processor.processor import (
    Processor as WithProcessorBase,
)
from .partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)
from .partials.with_pipeline_as_stage.pipeline_mixin import (
    PipelineMixin as WithPipelineAsStage,
)
from .partials.with_pipeline_as_stage.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsStageInterface,
)
from .partials.with_pipeline_as_immutable.pipeline_mixin import (
    PipelineMixin as WithPipelineAsImmutable,
)
from .partials.with_pipeline_as_immutable.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsImmutableInterface,
)
from .partials.with_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallable,
)
from .partials.with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)
from .partials.with_processor_commands.processing_strategy import (
    ProcessingStrategy,
)
from .partials.with_processor_commands.processing_strategy_interface import (
    ProcessingStrategyInterface,
)
from .partials.with_processor_commands.strategies.command_processing_strategy import (  # noqa
    CommandProcessingStrategy,
)
from .partials.with_processor_commands.strategies.processor_processing_strategy import (  # noqa
    ProcessorProcessingStrategy,
)
from .partials.with_processor_commands.traits.processable_as_command import (
    ProcessableAsCommand,
)


# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.15.0"

# Expose the public API
__all__ = [
    # Core
    "Command",
    "CommandInterface",
    "Pipeline",
    "PipelineInterface",
    "Stage",
    "StageInterface",
    "Processor",
    "ProcessorInterface",
    "PipelineFactory",
    "PipelineFactoryInterface",
    "ProcessingStrategy",
    "ProcessingStrategyInterface",
    # Traits
    "ProcessableAsCommand",
    # Types
    "T_in",
    "T_out",
    "StageCallable",
    # Processors
    "ChainedProcessor",
    "ChainedPipeline",
    "InterruptibleProcessor",
    "InterruptiblePipeline",
    # Strategies
    "CommandProcessingStrategy",
    "ProcessorProcessingStrategy",
    # Partials
    "WithPipelineBase",
    "WithPipelineBaseInterface",
    "WithStageBase",
    "WithStageBaseInterface",
    "WithPipelineAsList",
    "WithPipelineAsListInterface",
    "WithPipelineProcessor",
    "WithPipelineProcessorInterface",
    "WithProcessorBase",
    "WithProcessorBaseInterface",
    "WithPipelineAsStage",
    "WithPipelineAsStageInterface",
    "WithPipelineAsImmutable",
    "WithPipelineAsImmutableInterface",
    "WithStageAsCallable",
    "WithStageAsCallableInterface",
]
