from typing import Any

from ..command_interface import CommandInterface
from ...with_base.stage_callable import StageCallable
from ...with_base.types import T_in, T_out
from ..processing_strategy import ProcessingStrategy


class CommandProcessingStrategy(ProcessingStrategy[T_in, T_out]):
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        command = self._make_command(payload, stages, *args, **kwds)

        return await command.execute(*args, **kwds)

    def _make_command(
        self,
        payload: T_in,
        stages: list[StageCallable],
        *args: Any,
        **kwds: Any,
    ) -> CommandInterface[T_in, T_out]:
        if not self.processor.command_class:
            raise ValueError("Command class is not set")

        return self.processor.command_class(
            processor=self.processor,
            payload=payload,
            stages=stages,
            *args,
            **kwds,
        )
