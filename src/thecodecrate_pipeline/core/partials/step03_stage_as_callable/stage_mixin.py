from abc import ABC, abstractmethod
from typing import Any

from ..step01_base.types import T_in, T_out
from .stage_interface_mixin import (
    StageInterfaceMixin as ImplementsStageInterface,
)


class StageMixin(
    ImplementsStageInterface[T_in, T_out],
    ABC,
):
    @abstractmethod
    async def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        pass
