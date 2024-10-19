from __future__ import annotations
from abc import abstractmethod
from typing import Any, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from .processor_interface_mixin import (
        ProcessorInterfaceMixin as ProcessorInterface,
    )

from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class CommandInterface(
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        processor: ProcessorInterface,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    @abstractmethod
    async def execute(self) -> T_out: ...

    async def _call_stage(
        self, payload: T_in, stage: StageCallableType, *args: Any, **kwds: Any
    ) -> T_in: ...
