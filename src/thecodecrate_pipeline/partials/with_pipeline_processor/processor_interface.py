from abc import abstractmethod
from typing import Any, Protocol, TypeVar

from ...support.has_call_async import HasCallAsyncInterface
from ...support.clonable import ClonableInterface
from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType


class ProcessorInterface(
    HasCallAsyncInterface,
    ClonableInterface,
    Protocol[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: list[StageCallableType],
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        stage: StageCallableType,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> Any: ...


TProcessor = TypeVar(
    "TProcessor", bound=ProcessorInterface, infer_variance=True
)
