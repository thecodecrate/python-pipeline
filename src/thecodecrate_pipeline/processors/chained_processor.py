from typing import Any, cast

from ..partials.with_base.stage_callable import StageCallableType
from ..partials.with_base.types import T_in, T_out
from ..partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorConcern,
)


class ChainedProcessor(
    WithProcessorConcern[T_in, T_out],
    ImplementsProcessorInterface[T_in, T_out],
):
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call_stage(
                payload=payload, stage=stage, *args, **kwds
            )

        return cast(T_out, payload)
