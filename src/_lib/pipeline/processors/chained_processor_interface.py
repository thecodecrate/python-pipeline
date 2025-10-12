from typing import Any, Protocol

from ..callable_type import CallableCollection
from ..processor_interface import ProcessorInterface
from ..types import T_in, T_out


class ChainedProcessorInterface(
    ProcessorInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    """
    A processor that processes the payload through a series of stages.
    """

    async def process(
        self,
        payload: T_in,
        stages: CallableCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
