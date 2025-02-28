from abc import ABC

# extends: self-bridge concrete
from .._bridges.pipeline import Pipeline

# uses: bridge interface
from .._bridges.types import T_in, T_out

# uses: base concrete
from ..bases.processors.chained_processor import ChainedProcessor

# implements: self-interface
from .pipeline_interface_mixin import PipelineInterfaceMixin as ImplementsInterface


class PipelineMixin(
    Pipeline[T_in, T_out],
    ImplementsInterface[T_in, T_out],
    ABC,
):
    def _get_default_processor_class(self) -> type[ChainedProcessor[T_in, T_out]]:
        return ChainedProcessor[T_in, T_out]
