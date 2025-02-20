from typing import Protocol

# extends: outside base
from ..plugins._01_with_base import StageCallable as StageCallableBase
from ..plugins._01_with_base import (
    StageClassOrInstance,
    StageCollection,
    StageInstance,
    StageInstanceCollection,
)

# uses: bridge interface
from .types import T_in, T_out


class StageCallable(
    StageCallableBase[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


__all__ = (
    "StageCallable",
    "StageInstance",
    "StageInstanceCollection",
    "StageClassOrInstance",
    "StageCollection",
)
