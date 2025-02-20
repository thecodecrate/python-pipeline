from abc import ABC, abstractmethod
from typing import Any

# uses: bridge
from ..bridges.types import T_in, T_out

# implements: self-interface
from .stage_interface_mixin import StageInterfaceMixin as ImplementsInterface


class StageMixin(
    ImplementsInterface[T_in, T_out],
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
        """
        Runs the stage.
        """
        pass
