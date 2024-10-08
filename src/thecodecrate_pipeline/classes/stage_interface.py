from typing import Protocol

from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..partials.with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)


class StageInterface(
    WithStageAsCallableInterface[T_in, T_out],
    WithStageBaseInterface,
    Protocol[T_in, T_out],
):
    pass
