from typing import Any, Awaitable, Protocol

from .types import T_in, T_out


class CallableType(
    Protocol[T_in, T_out],
):
    """Protocol for callable stages that process data in a pipeline."""

    def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out | Awaitable[T_out]: ...


CallableCollection = tuple[CallableType, ...]
"""Collection of objects or functions used as stages in the pipeline"""

StageDefinition = CallableType | type[CallableType]
"""A Stage class, object or function"""

StageDefinitionCollection = tuple[StageDefinition, ...]
"""Collection of Stage classes, objects or functions used to define stages in the pipeline"""
