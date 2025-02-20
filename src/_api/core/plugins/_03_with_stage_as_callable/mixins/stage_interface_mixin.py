from abc import abstractmethod
from typing import Any, Protocol

# extends: self-bridge
from ..bridges.stage_interface import StageInterface

# uses: bridge
from ..bridges.types import T_in, T_out


class StageInterfaceMixin(
    StageInterface,
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
