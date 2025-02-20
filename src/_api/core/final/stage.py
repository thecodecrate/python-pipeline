# extends: outside base
from ..plugins._01_with_base import Stage as StageBase

# extends: outside mixins
from ..plugins._03_with_stage_as_callable import (
    StageMixin as _03_WithStageAsCallable,
)

# implements: self-interface
from .stage_interface import StageInterface as ImplementsInterface

# uses: bridge
from .types import T_in, T_out


class Stage(
    _03_WithStageAsCallable[T_in, T_out],
    StageBase,
    ImplementsInterface[T_in, T_out],
):
    pass
