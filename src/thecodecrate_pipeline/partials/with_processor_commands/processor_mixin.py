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
    strategy_class: Optional[type[ProcessingStrategyInterface]] = None
    strategy_instance: ProcessingStrategyInterface

    def __init__(
        self,
        command_class: Optional[type[CommandInterface]] = None,
        strategy_class: Optional[type[ProcessingStrategyInterface]] = None,
        strategy_instance: Optional[ProcessingStrategyInterface] = None,
        strategy: Optional[
            type[ProcessingStrategyInterface] | ProcessingStrategyInterface
        ] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if command_class:
            self.command_class = command_class

        if strategy_class:
            self.strategy_class = strategy_class

        if strategy_instance:
            self.strategy_instance = strategy_instance

        if strategy:
            cloned = self.with_strategy(strategy)

            self.strategy_class = cloned.strategy_class

            self.strategy_instance = cloned.strategy_instance

        if not self.strategy_class:
            self.strategy_class = self.which_strategy_class()

        if not hasattr(self, "strategy_instance"):
            self.strategy_instance = self._make_strategy()

    def with_command_class(
        self, command_class: type[CommandInterface]
    ) -> Self:
        return self.clone({"command_class": command_class})

    def with_strategy(
        self,
        strategy: (
            type[ProcessingStrategyInterface[T_in, T_out]]
            | ProcessingStrategyInterface[T_in, T_out]
        ),
    ) -> Self:
        if isinstance(strategy, type):
            return self.with_strategy_class(strategy)

        return self.with_strategy_instance(strategy)

    def with_strategy_instance(
        self, strategy_instance: ProcessingStrategyInterface[T_in, T_out]
    ) -> Self:
        return self.clone(
            {
                "strategy_class": strategy_instance.__class__,
                "strategy_instance": strategy_instance,
            }
        )

    def with_strategy_class(
        self,
        strategy_class: type[ProcessingStrategyInterface[T_in, T_out]],
    ) -> Self:
        cloned = self.clone({"strategy_class": strategy_class})

        cloned.strategy_instance = strategy_class(cloned)

        return cloned

    def which_strategy_class(
        self,
    ) -> type[ProcessingStrategyInterface[T_in, T_out]]:
        if self.strategy_class:
            return self.strategy_class

        if self.command_class:
            return CommandProcessingStrategy

        return ProcessorProcessingStrategy

    def _make_strategy(
        self,
    ) -> ProcessingStrategyInterface[T_in, T_out]:
        strategy_class = self.which_strategy_class()

        return strategy_class(processor=self)

    async def process_with_strategy(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        return await self.strategy_instance.process(
            payload, stages, *args, **kwds
        )

    # let's turn `process` as a not abstract method
    # having `process` as abstract will cause an exception on
    # command processors
    # that's because processors with the "command" strategy
    # don't have to implement the `process` method
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        raise NotImplementedError("Processor.process() must be implemented.")
