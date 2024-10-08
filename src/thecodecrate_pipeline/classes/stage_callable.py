from typing import Protocol

from ..partials.with_base.types import T_in, T_out
from ..partials.with_base.stage_callable import (
    StageCallable as WithStageCallableBase,
)


class StageCallable(
    WithStageCallableBase[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
