from typing import Any, Awaitable, Protocol

from .types import T_in, T_out


class StageCallable(
    Protocol[T_in, T_out],
):
    """Callable object used in the pipeline"""

    def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out | Awaitable[T_out]: ...


StageInstance = StageCallable
"""Stage object"""

StageInstanceCollection = tuple[StageInstance, ...]
"""Collection of Stage objects"""

StageClassOrInstance = StageInstance | type[StageInstance]
"""Stage class or object"""

StageCollection = tuple[StageClassOrInstance, ...]
"""Collection of Stage classes or objects"""
