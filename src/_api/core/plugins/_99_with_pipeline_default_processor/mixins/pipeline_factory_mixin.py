from typing import Generic

# uses: bridge interface
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
    def _get_default_pipeline_class(self) -> type[Pipeline[T_in, T_out]]:
        return Pipeline[T_in, T_out]
