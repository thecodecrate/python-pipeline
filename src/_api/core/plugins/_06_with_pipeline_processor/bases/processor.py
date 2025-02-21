from abc import abstractmethod
from typing import Any

# extends: 3rd-party concrete
from ....support.clonable import Clonable
from ....support.has_call_async import HasCallAsync

# uses: bridge interface
from ..bridges.stage_callable import StageInstance, StageInstanceCollection
from ..bridges.types import T_in, T_out

# implements: self-interface
from .processor_interface import ProcessorInterface as ImplementsInterface


class Processor(
    HasCallAsync,
    Clonable,
    ImplementsInterface[T_in, T_out],
):
    def __init__(self, *args: Any, **kwds: Any) -> None:
        """Constructor."""
        pass

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

        Args:
            payload (T_in): The input payload to process.
            stages (StageInstanceCollection): The collection of stages to process the payload through.
            *args (Any): Additional positional arguments.
            **kwds (Any): Additional keyword arguments.

        Returns:
            T_out: The processed output.
        """
        pass

    # HasCallAsync: include callable type and `payload` in the signature
    async def _call(
        self,
        callable: StageInstance,
        payload: T_in,
        *args: Any,
        **kwds: Any,
    ) -> Any:
        """
        Alias to `process` method.
        """
        return await super()._call(callable, payload, *args, **kwds)
