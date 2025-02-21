from abc import abstractmethod
from typing import Any, Protocol, TypeVar

# extends: 3rd-party interface
from ....support.clonable import ClonableInterface
from ....support.has_call_async import HasCallAsyncInterface

# uses: bridge interface
from ..bridges.stage_callable import StageInstance, StageInstanceCollection
from ..bridges.types import T_in, T_out


class ProcessorInterface(
    HasCallAsyncInterface,
    ClonableInterface,
    Protocol[T_in, T_out],
):
    def __init__(self, *args: Any, **kwds: Any) -> None: ...

    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: StageInstanceCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        callable: StageInstance,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> Any: ...


TProcessor = TypeVar("TProcessor", bound=ProcessorInterface, infer_variance=True)
