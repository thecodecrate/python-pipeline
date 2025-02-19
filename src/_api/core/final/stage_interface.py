from typing import Protocol

from ..partials.step01_base import Stage_Base_Interface
from ..partials.step03_stage_as_callable import Stage_WithStageAsCallable_Interface
from .types import T_in, T_out


class StageInterface(
    Stage_WithStageAsCallable_Interface[T_in, T_out],
    Stage_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
