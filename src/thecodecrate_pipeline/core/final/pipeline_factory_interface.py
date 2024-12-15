from typing import Protocol

from ..partials.step01_base.pipeline_interface import PipelineInterface
from ..partials.step05_pipeline_factory.pipeline_factory_interface import (
    PipelineFactoryInterface as WithPipelineFactoryBaseInterface,
)
from ..partials.step06_pipeline_processor.pipeline_factory_interface_mixin import (  # noqa
    PipelineFactoryInterfaceMixin as WithProcessorInterface,
)


class PipelineFactoryInterface(
    WithProcessorInterface,
    WithPipelineFactoryBaseInterface[PipelineInterface],
    Protocol,
):
    pass
