from typing import Any, cast

from ...core.final.processor import Processor
from ...core.final.stage_callable import StageInstanceCollection
from ...core.final.types import T_in, T_out


class ChainedProcessor(Processor[T_in, T_out]):
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call(stage=stage, payload=payload, *args, **kwds)

        return cast(T_out, payload)
