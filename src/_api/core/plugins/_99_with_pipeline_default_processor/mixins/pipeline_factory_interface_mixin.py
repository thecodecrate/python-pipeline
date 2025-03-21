from typing import Protocol

# extends: self-bridge
from .._bridges.pipeline_factory_interface import PipelineFactoryInterface

# uses: bridge interface
from .._bridges.types import T_in, T_out


class PipelineFactoryInterfaceMixin(
    PipelineFactoryInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
