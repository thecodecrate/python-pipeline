from typing import Protocol

# extends: outside base
from ..._01_with_base import StageInterface as StageBaseInterface

# extends: outside mixins
from ..._03_with_stage_as_callable import (
    StageInterfaceMixin as _03_WithStageAsCallableInterface,
)

# uses: bridge interface
from .types import T_in, T_out


class StageInterface(
    _03_WithStageAsCallableInterface[T_in, T_out],
    StageBaseInterface,
    Protocol[T_in, T_out],
):
    pass
