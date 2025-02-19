from abc import abstractmethod
from typing import Any

from ...support.clonable import Clonable
from ...support.has_call_async import HasCallAsync
from ..step01_base import (
    StageInstance,
    StageInstanceCollection,
    T_in,
    T_out,
)
from .processor_interface import (
    ProcessorInterface as ImplementsInterface,
)


class Processor(
    HasCallAsync,
    Clonable,
    ImplementsInterface[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        """
        Process the given payload through the provided stages.
        """
        pass

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        stage: StageInstance,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> Any:
        """
        Alias to `process` method.
        """
        return await super()._call(stage, payload, *args, **kwds)
