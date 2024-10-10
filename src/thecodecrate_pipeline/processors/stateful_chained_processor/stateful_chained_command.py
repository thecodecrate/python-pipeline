from typing import cast

from ...classes.command import Command
from ...partials.with_base.types import T_in, T_out


class StatefulChainedCommand(Command[T_in, T_out]):
    async def execute(self) -> T_out:
        for stage in self.stages:
            self.payload = await self._call_stage(
                payload=self.payload,
                stage=stage,
                *self.extra_args,
                **self.extra_kwds,
            )

        return cast(T_out, self.payload)
