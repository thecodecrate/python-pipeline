from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .processor_mixin import ProcessorMixin as Processor

from .processing_strategy_interface import ProcessingStrategyInterface
from ..with_base.stage_callable import StageCallable
from ..with_base.types import T_in, T_out


class ProcessingStrategy(ProcessingStrategyInterface[T_in, T_out]):
    processor: Processor

    def __init__(self, processor: Processor, *args: Any, **kwds: Any) -> None:
        self.processor = processor

    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
