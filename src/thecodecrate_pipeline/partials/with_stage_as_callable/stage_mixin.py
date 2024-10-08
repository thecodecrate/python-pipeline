from abc import ABC, abstractmethod
from typing import Any

from .stage_interface_mixin import (
    StageInterfaceMixin as ImplementsStageInterface,
)
from ..with_base.types import T_in, T_out


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
