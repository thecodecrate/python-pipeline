from abc import abstractmethod
from typing import Any, Protocol

from ..with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..with_base.types import T_in, T_out


class StageInterfaceMixin(
    WithStageBaseInterface,
    Protocol[T_in, T_out],
):
    @abstractmethod
    async def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
