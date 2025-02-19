from typing import Any, cast

from ...step01_base.stage_callable import StageInstanceCollection
from ...step01_base.types import T_in, T_out
from ...step06_pipeline_processor.processor import Processor


class ChainedProcessor(Processor[T_in, T_out]):
    """
    A processor that processes the payload through a series of stages.
    """

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
