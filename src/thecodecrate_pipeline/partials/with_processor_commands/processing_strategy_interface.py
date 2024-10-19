from __future__ import annotations
from abc import abstractmethod
from typing import Any, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from .processor_interface_mixin import (
        ProcessorInterfaceMixin as ProcessorInterface,
    )

from ..with_base.stage_callable import StageCallable
from ..with_base.types import T_in, T_out


class ProcessingStrategyInterface(Protocol[T_in, T_out]):
    def __init__(
        self, processor: ProcessorInterface, *args: Any, **kwds: Any
    ) -> None: ...

    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
