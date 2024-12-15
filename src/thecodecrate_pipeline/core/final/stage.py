from abc import ABC

from ..partials.step01_base.stage import (
    Stage as WithStageBaseConcern,
)
from ..partials.step01_base.types import T_in, T_out
from ..partials.step03_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallableConcern,
)
from .stage_interface import StageInterface as ImplementsStageInterface


class Stage(
    WithStageAsCallableConcern[T_in, T_out],
    WithStageBaseConcern,
    ImplementsStageInterface,
    ABC,
):
    pass
