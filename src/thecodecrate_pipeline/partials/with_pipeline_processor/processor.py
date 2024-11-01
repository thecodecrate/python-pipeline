from abc import ABC, abstractmethod
from typing import Any

from ...support.has_call_async import HasCallAsync
from ...support.clonable import Clonable
from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import (
    StageInstance,
    StageInstanceCollection,
)


class Processor(
    HasCallAsync,
    Clonable,
    ImplementsProcessorInterface[T_in, T_out],
    ABC,
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        pass

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        stage: StageInstance,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> Any:
        return await super()._call(stage, payload, *args, **kwds)
