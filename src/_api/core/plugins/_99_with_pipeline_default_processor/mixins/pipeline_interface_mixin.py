from typing import Protocol

# extends: self-bridge
from ..bridges.pipeline_interface import PipelineInterface

# uses: bridge interface
from ..bridges.types import T_in, T_out


class PipelineInterfaceMixin(
    PipelineInterface,
    Protocol[T_in, T_out],
):
    pass
