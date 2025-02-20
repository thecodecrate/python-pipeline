from typing import Any, Protocol

# extends: "3rd-party" interface
from ...bridges.processor_interface import ProcessorInterface

# uses: bridge interface
from ...bridges.stage_callable import StageInstanceCollection
from ...bridges.types import T_in, T_out


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
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
