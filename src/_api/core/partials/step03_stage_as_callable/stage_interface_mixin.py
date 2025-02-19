from abc import abstractmethod
from typing import Any, Protocol

from ..step01_base import (
    Stage_Base_Interface,
    T_in,
    T_out,
)


class StageInterfaceMixin(
    Stage_Base_Interface,
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
