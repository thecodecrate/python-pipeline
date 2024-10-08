from abc import abstractmethod
from typing import Any

from .stage_interface_mixin import (
    StageInterfaceMixin as ImplementsStageInterface,
)
from ..with_base.payload_type import TPayload


class StageMixin(
    ImplementsStageInterface[TPayload],
):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass
