from typing import Any, cast

# extends: "3rd-party" concrete
from ...bridges.processor import Processor

# uses: bridge interface
from ...bridges.stage_callable import StageInstanceCollection
from ...bridges.types import T_in, T_out

# implements: self-interface
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
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call(callable=stage, payload=payload, *args, **kwds)

        return cast(T_out, payload)
