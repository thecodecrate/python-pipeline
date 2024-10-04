from abc import abstractmethod
from typing import Any, Protocol

from ..with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..with_base.type_payload import TPayload


class StageInterfaceMixin(
    WithStageBaseInterface,
    Protocol[TPayload],
):
    @abstractmethod
    async def __call__(
        self,
        payload: TPayload,
        *args: Any,
        **kwds: Any,
    ) -> TPayload: ...
