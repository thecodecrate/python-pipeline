from typing import Protocol

from ..partials.with_base.pipeline_interface import PipelineInterface
from ..partials.with_pipeline_factory.pipeline_factory_interface import (
    PipelineFactoryInterface as WithPipelineFactoryBaseInterface,
)
from ..partials.with_pipeline_processor.pipeline_factory_interface_mixin import (  # noqa
    PipelineFactoryInterfaceMixin as WithProcessorInterface,
)


class PipelineFactoryInterface(
    WithProcessorInterface,
    WithPipelineFactoryBaseInterface[PipelineInterface],
    Protocol,
):
    pass
