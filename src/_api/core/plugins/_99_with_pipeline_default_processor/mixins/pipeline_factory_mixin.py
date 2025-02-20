from typing import Generic, Optional

# uses: bridge interface
from ..bridges.pipeline_interface import TPipeline
from ..bridges.types import T_in, T_out

# implements: self-interface
from .pipeline_factory_interface_mixin import (
    PipelineFactoryInterfaceMixin as ImplementsInterface,
)

# uses: mixin-bridge concrete
from .pipeline_mixin import PipelineMixin as Pipeline


class PipelineFactoryMixin(
    ImplementsInterface[T_in, T_out],
    Generic[T_in, T_out],
):
    pipeline_class: Optional[type[TPipeline]] = Pipeline[T_in, T_out]
