from abc import abstractmethod
from typing import Any, Awaitable, Protocol

from ..support.clonable.clonable_interface import ClonableInterface
from ..types.callable_type import CallableCollection, CallableType
from ..types.types import T_in, T_out


class Processor(
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
