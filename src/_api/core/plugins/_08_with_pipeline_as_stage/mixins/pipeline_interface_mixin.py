from typing import Protocol

# extends: self-bridge
from ..bridges.pipeline_interface import PipelineInterface

# extends: bridge interface
from ..bridges.stage_interface import StageInterface

# uses: bridge interface
from ..bridges.types import T_in, T_out


class PipelineInterfaceMixin(
    StageInterface[T_in, T_out],
    PipelineInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
