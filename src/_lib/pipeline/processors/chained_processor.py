from typing import Any, cast

from ..callable_type import CallableCollection
from ..processor import Processor
from ..types import T_in, T_out
from .chained_processor_interface import (
    ChainedProcessorInterface as ImplementsInterface,
)


class ChainedProcessor(
    Processor[T_in, T_out],
    ImplementsInterface[T_in, T_out],
):
    async def process(
        self,
        payload: T_in,
        stages: CallableCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        """
        Process the given payload through the provided stages.

        Args:
            payload (T_in): The input payload to process.
            stages (CallableCollection): The collection of stages to process the payload through.
            *args (Any): Additional positional arguments.
            **kwds (Any): Additional keyword arguments.

        Returns:
            T_out: The processed output.
        """
        payload_out: Any = payload

        for stage in stages:
            payload_out = await self._call(
                callable=stage, payload=payload_out, *args, **kwds
            )

        return cast(T_out, payload_out)
