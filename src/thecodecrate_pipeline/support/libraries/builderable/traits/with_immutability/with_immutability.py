import copy
from abc import ABC
from typing import Generic, cast
from .parent_class import TParentClass
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class WithImmutability(
    Generic[TParentClass, TBuilderOutput, TBuilderPart],
    ABC,
):
    def clone(self) -> TParentClass:
        this = cast(TParentClass, self)

        cloned = cast(TParentClass, self.__class__())

        cloned.parts = copy.deepcopy(this.parts)

        return cloned

    def add(
        self,
        part: TBuilderPart,
    ) -> TParentClass:
        cloned = self.clone()

        cloned.parts.append(part)

        return cloned
