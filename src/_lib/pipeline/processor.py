import inspect
from abc import abstractmethod
from typing import Any

from .callable_type import CallableCollection, CallableType
from .processor_interface import ProcessorInterface as ImplementsInterface
from .traits.clonable import Clonable
from .types import T_in, T_out


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
        Process the given payload.
        """
        result = callable(payload, *args, **kwds)

        if inspect.isawaitable(result):
            return await result

        return result
