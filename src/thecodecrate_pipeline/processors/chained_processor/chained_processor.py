from typing import Any, cast

from ...classes.stage_callable import StageInstanceCollection
from ...classes.types import T_in, T_out
from ...classes.processor import Processor


class ChainedProcessor(Processor[T_in, T_out]):
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call(
                stage=stage, payload=payload, *args, **kwds
            )

        return cast(T_out, payload)
