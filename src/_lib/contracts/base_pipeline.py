from typing import Protocol

from ..support.clonable import ClonableInterface
from ..types.types import T_in, T_out


class BasePipeline(
    ClonableInterface,
    Protocol[T_in, T_out],
):
    pass
