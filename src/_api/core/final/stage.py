from abc import ABC

from ..partials.step01_base import Stage_Base
from ..partials.step03_stage_as_callable import Stage_WithStageAsCallable
from .stage_interface import StageInterface as ImplementsInterface
from .types import T_in, T_out


class Stage(
    Stage_WithStageAsCallable[T_in, T_out],
    Stage_Base,
    ImplementsInterface[T_in, T_out],
    ABC,
):
    pass
