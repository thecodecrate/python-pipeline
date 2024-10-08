from abc import ABC

from .stage_interface import StageInterface as ImplementsStageInterface
from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.stage import (
    Stage as WithStageBaseConcern,
)
from ..partials.with_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallableConcern,
)


class Stage(
    WithStageAsCallableConcern[T_in, T_out],
    WithStageBaseConcern,
    ImplementsStageInterface,
    ABC,
):
    pass
