from .classes.pipeline_builder import PipelineBuilder
from .classes.pipeline_builder_interface import PipelineBuilderInterface
from .classes.pipeline import Pipeline
from .classes.pipeline_interface import PipelineInterface
from .classes.processor import Processor
from .classes.processor_interface import ProcessorInterface
from .classes.stage import Stage
from .classes.stage_interface import StageInterface
from .processors.chained_processor import ChainedProcessor
from .processors.interruptible_processor import InterruptibleProcessor
from .partials.with_base.type_payload import TPayload
from .partials.with_base.type_pipeline_callable import PipelineCallable
from .partials.with_base.pipeline import Pipeline as WithPipelineBase
from .partials.with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from .partials.with_base.stage import Stage as WithStageBase
from .partials.with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from .partials.with_builder_methods.pipeline_mixin import (
    PipelineMixin as WithBuilderMethods,
)
from .partials.with_builder_methods.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithBuilderMethodsInterface,
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
from .partials.with_pipelineable_methods.pipeline_mixin import (
    PipelineMixin as WithPipelineableMethods,
)
from .partials.with_pipelineable_methods.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineableMethodsInterface,
)
from .partials.with_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallable,
)
from .partials.with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)


# Version of the package
# DO NOT MODIFY MANUALLY
# This will be updated by `bumpver` command.
# - Make sure to commit all changes first before running `bumpver`.
# - Run `bumpver update --[minor|major|patch]`
__version__ = "1.10.0"

# Expose the public API
__all__ = [
    # Core
    "Pipeline",
    "PipelineInterface",
    "Stage",
    "StageInterface",
    "Processor",
    "ProcessorInterface",
    "PipelineBuilder",
    "PipelineBuilderInterface",
    # Types
    "TPayload",
    "PipelineCallable",
    # Processors
    "ChainedProcessor",
    "InterruptibleProcessor",
    # Partials
    "WithPipelineBase",
    "WithPipelineBaseInterface",
    "WithStageBase",
    "WithStageBaseInterface",
    "WithBuilderMethods",
    "WithBuilderMethodsInterface",
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
    "WithPipelineableMethods",
    "WithPipelineableMethodsInterface",
    "WithStageAsCallable",
    "WithStageAsCallableInterface",
]
