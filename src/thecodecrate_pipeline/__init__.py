from .core.final.pipeline import Pipeline
from .core.final.pipeline_factory import PipelineFactory
from .core.final.pipeline_factory_interface import PipelineFactoryInterface
from .core.final.pipeline_interface import PipelineInterface
from .core.final.processor import Processor
from .core.final.processor_interface import ProcessorInterface
from .core.final.stage import Stage
from .core.final.stage_interface import StageInterface
from .core.final.types import T_in, T_out
from .core.partials.step01_base.pipeline import Pipeline as WithPipelineBase
from .core.partials.step01_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from .core.partials.step01_base.stage import Stage as WithStageBase
from .core.partials.step01_base.stage_callable import (
    StageCallable,
    StageClassOrInstance,
    StageCollection,
    StageInstance,
    StageInstanceCollection,
)
from .core.partials.step01_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from .core.partials.step02_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from .core.partials.step02_pipeline_as_list.pipeline_mixin import (
    PipelineMixin as WithPipelineAsList,
)
from .core.partials.step03_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)
from .core.partials.step03_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallable,
)
from .core.partials.step06_pipeline_processor.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineProcessorInterface,
)
from .core.partials.step06_pipeline_processor.pipeline_mixin import (
    PipelineMixin as WithPipelineProcessor,
)
from .core.partials.step06_pipeline_processor.processor import (
    Processor as WithProcessorBase,
)
from .core.partials.step06_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)
from .core.partials.step07_pipeline_as_stage.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsStageInterface,
)
from .core.partials.step07_pipeline_as_stage.pipeline_mixin import (
    PipelineMixin as WithPipelineAsStage,
)
from .processors.chained_processor.chained_pipeline import ChainedPipeline
from .processors.chained_processor.chained_processor import ChainedProcessor
from .processors.interruptible_processor.interruptible_pipeline import (
    InterruptiblePipeline,
)
from .processors.interruptible_processor.interruptible_processor import (
    InterruptibleProcessor,
)

# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.23.0"

# Expose the public API
__all__ = [
    # Core
    "Pipeline",
    "PipelineInterface",
    "Stage",
    "StageInterface",
    "Processor",
    "ProcessorInterface",
    "PipelineFactory",
    "PipelineFactoryInterface",
    # Types
    "T_in",
    "T_out",
    "StageCallable",
    "StageInstance",
    "StageInstanceCollection",
    "StageClassOrInstance",
    "StageCollection",
    # Processors
    "ChainedProcessor",
    "ChainedPipeline",
    "InterruptibleProcessor",
    "InterruptiblePipeline",
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
    "WithStageAsCallable",
    "WithStageAsCallableInterface",
]
