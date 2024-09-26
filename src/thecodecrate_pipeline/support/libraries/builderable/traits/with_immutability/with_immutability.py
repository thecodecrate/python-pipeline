import copy
from abc import ABC
from typing import Generic, cast
from .parent_class import TParentClass
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class WithImmutability(
    Generic[TParentClass, TBuilderOutput, TBuilderPart],
    ABC,
):
    def add(
        self,
        part: TBuilderPart,
    ) -> TParentClass:
        this = cast(TParentClass, self)

        cloned = copy.deepcopy(this)

        cloned.get_parts().append(part)

        return cloned
