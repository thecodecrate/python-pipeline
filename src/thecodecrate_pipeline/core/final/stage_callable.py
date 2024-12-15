from typing import Protocol

from ..partials.step01_base.stage_callable import (
    StageCallable as WithStageCallableBase,
)
from ..partials.step01_base.stage_callable import (
    StageClassOrInstance,
    StageCollection,
    StageInstanceCollection,
)
from ..partials.step01_base.types import T_in, T_out


class StageCallable(
    WithStageCallableBase[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


__all__ = [
    "StageCallable",
    "StageCollection",
    "StageInstanceCollection",
    "StageClassOrInstance",
]
