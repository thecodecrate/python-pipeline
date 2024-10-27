from __future__ import annotations
from typing import Any, Optional, Protocol, Self
import typing

if typing.TYPE_CHECKING:
    from .processing_strategy_interface import ProcessingStrategyInterface
    from .command_interface import CommandInterface

from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType
from ..with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)


class ProcessorInterfaceMixin(
    WithProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
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
    ) -> None: ...

    def with_command_class(
        self, command_class: type[CommandInterface]
    ) -> Self: ...

    def with_strategy(
        self,
        strategy: (
            type[ProcessingStrategyInterface[T_in, T_out]]
            | ProcessingStrategyInterface[T_in, T_out]
        ),
    ) -> Self: ...

    def with_strategy_instance(
        self, strategy_instance: ProcessingStrategyInterface[T_in, T_out]
    ) -> Self: ...

    def with_strategy_class(
        self,
        strategy_class: type[ProcessingStrategyInterface[T_in, T_out]],
    ) -> Self: ...

    def which_strategy_class(
        self,
    ) -> type[ProcessingStrategyInterface[T_in, T_out]]: ...

    def _make_strategy(
        self,
    ) -> ProcessingStrategyInterface[T_in, T_out]: ...

    async def process_with_strategy(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

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
    ) -> T_out: ...
