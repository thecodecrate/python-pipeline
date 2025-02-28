from typing import Protocol

# extends: outside base
from ..._01_with_base import StageCallable as StageCallableBase

# uses: local bridge
from .types import T_in, T_out


class StageCallable(
    StageCallableBase[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


StageInstance = StageCallable

StageInstanceCollection = tuple[StageInstance, ...]

StageClassOrInstance = StageInstance | type[StageInstance]

StageCollection = tuple[StageClassOrInstance, ...]
