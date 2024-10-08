from typing import Protocol

from ..with_base.types import T_in, T_out
from ..with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)


class StageFacade(
    WithStageAsCallableInterface[T_in, T_out],
    WithStageBaseInterface,
    Protocol[T_in, T_out],
):
    pass
