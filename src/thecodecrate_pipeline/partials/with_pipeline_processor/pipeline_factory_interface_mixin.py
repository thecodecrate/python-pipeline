from typing import Protocol, Self

from .processor_interface import ProcessorInterface
from ..with_base.pipeline_interface import PipelineInterface
from ..with_pipeline_factory.pipeline_factory_interface import (
    PipelineFactoryInterface as WithPipelineFactoryBaseInterface,
)


class PipelineFactoryInterfaceMixin(
    WithPipelineFactoryBaseInterface[PipelineInterface],
    Protocol,
):
    def with_processor(self, processor: ProcessorInterface) -> Self: ...

    def with_processor_class(
        self, processor_class: type[ProcessorInterface]
    ) -> Self: ...
