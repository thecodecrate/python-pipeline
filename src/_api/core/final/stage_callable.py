from typing import Protocol

from ..partials.step01_base import (
    StageCallable_Base,
    StageClassOrInstance,
    StageCollection,
    StageInstance,
    StageInstanceCollection,
)
from .types import T_in, T_out


class StageCallable(
    StageCallable_Base[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


__all__ = (
    "StageCallable",
    "StageCollection",
    "StageInstance",
    "StageInstanceCollection",
    "StageClassOrInstance",
)
