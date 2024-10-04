from abc import abstractmethod
from typing import Any, Protocol

from .stage_interface_mixin import (
    StageInterfaceMixin as ImplementsStageInterface,
)
from ..with_base.type_payload import TPayload


class StageMixin(
    ImplementsStageInterface[TPayload],
    Protocol[TPayload],
):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload:
        pass
