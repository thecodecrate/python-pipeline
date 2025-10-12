from abc import abstractmethod
from typing import Any, Awaitable, Protocol

from .callable_type import CallableCollection, CallableType
from .traits.clonable import ClonableInterface
from .types import T_in, T_out


class ProcessorInterface(
    ClonableInterface,
    Protocol[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: CallableCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    async def _call(
        self,
        callable: CallableType[T_in, T_out | Awaitable[T_out]],
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...
