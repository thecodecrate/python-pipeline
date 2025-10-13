from abc import ABC
from typing import Any, Generic

from ..support.clonable import Clonable
from ..types.types import T_in, T_out


class BasePipeline(
    Clonable,
    Generic[T_in, T_out],
    ABC,
):
    def __init__(
        self,
        *args: Any,
        **kwds: Any,
    ) -> None:
        pass
