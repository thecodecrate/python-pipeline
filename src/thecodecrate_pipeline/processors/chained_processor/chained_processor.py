from typing import Any, cast

from ...classes.stage_callable import StageCallable
from ...classes.types import T_in, T_out
from ...classes.processor import Processor
from .chained_command import ChainedCommand


class ChainedProcessor(Processor[T_in, T_out]):
    command_class = ChainedCommand

    async def process(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        for stage in stages:
            payload = await self._call_stage(
                payload=payload, stage=stage, *args, **kwds
            )

        return cast(T_out, payload)
