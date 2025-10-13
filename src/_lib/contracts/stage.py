from abc import abstractmethod
from typing import Any, Protocol

from ..types.types import T_in, T_out


class Stage(
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
