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
        processing_strategy: Optional[
            type[ProcessingStrategyInterface]
        ] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    def with_processing_strategy(
        self, processing_strategy: ProcessingStrategyInterface[T_in, T_out]
    ) -> Self: ...

    def which_processing_strategy_class(
        self,
    ) -> type[ProcessingStrategyInterface[T_in, T_out]]: ...

    def _make_processing_strategy(
        self,
    ) -> ProcessingStrategyInterface[T_in, T_out]: ...

    async def process_with_strategy(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    # make `process` method not abstract
    # when using command strategy, the `process` method is not used
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
