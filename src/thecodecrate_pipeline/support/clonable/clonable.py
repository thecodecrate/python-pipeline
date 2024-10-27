import copy
from typing import Any, Protocol, Self

from .clonable_interface import ClonableInterface


class Clonable(ClonableInterface, Protocol):
    def clone(self, attributes: dict[str, Any]) -> Self:
        cloned = copy.deepcopy(self)

        for key, value in attributes.items():
            setattr(cloned, key, value)

        return cloned
