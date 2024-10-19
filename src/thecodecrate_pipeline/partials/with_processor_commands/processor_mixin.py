import copy
from abc import ABC
from typing import Any, Generic, Optional, Self

from .strategies.command_processing_strategy import CommandProcessingStrategy
from .strategies.processor_processing_strategy import (
    ProcessorProcessingStrategy,
)
from .processing_strategy_interface import ProcessingStrategyInterface
from .command_interface import CommandInterface
from .processor_interface_mixin import (
    ProcessorInterfaceMixin as ImplementsProcessorInterface,
)
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class ProcessorMixin(
    ImplementsProcessorInterface[T_in, T_out],
    Generic[T_in, T_out],
    ABC,
):
    command_class: Optional[type[CommandInterface]] = None
    processing_strategy: Optional[type[ProcessingStrategyInterface]] = None
    processing_strategy_instance: ProcessingStrategyInterface

    def __init__(
        self,
        command_class: Optional[type[CommandInterface]] = None,
        processing_strategy: Optional[
            type[ProcessingStrategyInterface]
        ] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        self.command_class = command_class or self.command_class

        self.processing_strategy = (
            processing_strategy or self.which_processing_strategy_class()
        )

        self.processing_strategy_instance = self._make_processing_strategy()

    def with_processing_strategy(
        self, processing_strategy: ProcessingStrategyInterface[T_in, T_out]
    ) -> Self:
        cloned = copy.deepcopy(self)

        cloned.processing_strategy_instance = processing_strategy

        return cloned

    def with_processing_strategy_class(
        self,
        processing_strategy_class: type[
            ProcessingStrategyInterface[T_in, T_out]
        ],
    ) -> Self:
        cloned = copy.deepcopy(self)

        cloned.processing_strategy = processing_strategy_class

        cloned.processing_strategy_instance = processing_strategy_class(cloned)

        return cloned

    def which_processing_strategy_class(
        self,
    ) -> type[ProcessingStrategyInterface[T_in, T_out]]:
        if self.processing_strategy:
            return self.processing_strategy

        if self.command_class:
            return CommandProcessingStrategy

        return ProcessorProcessingStrategy

    def _make_processing_strategy(
        self,
    ) -> ProcessingStrategyInterface[T_in, T_out]:
        strategy = self.which_processing_strategy_class()

        return strategy(processor=self, command_class=self.command_class)

    async def process_with_strategy(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await self.processing_strategy_instance.process(
            payload, stages, *args, **kwds
        )

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        raise NotImplementedError("Processor.process() must be implemented.")
