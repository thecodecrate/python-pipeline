import inspect
from abc import abstractmethod
from typing import Any

from .contracts.processor import Processor as ImplementsInterface
from .support.clonable import Clonable
from .types.callable_type import CallableCollection, CallableType
from .types.types import T_in, T_out


class Processor(
    Clonable,
    ImplementsInterface[T_in, T_out],
):
    @abstractmethod
    async def process(
        self,
        payload: T_in,
        stages: CallableCollection,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        """
        Process the given payload through the provided stages.

        Args:
            payload (T_in): The input payload to process.
            stages (CallableCollection): The collection of stages to process the payload through.
            *args (Any): Additional positional arguments.
            **kwds (Any): Additional keyword arguments.

        Returns:
            T_out: The processed output.
        """
        pass

    async def _call(
        self,
        callable: CallableType[T_in, T_out],
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        """
        Do the actual processing of the payload - the "process" method is just an alias to this method.
        """
        result = callable(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
