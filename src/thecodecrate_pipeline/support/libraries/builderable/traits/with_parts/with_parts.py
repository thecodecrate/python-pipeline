from abc import ABC, abstractmethod
from typing import Generic, Any, cast
from .parent_class import TParentClass
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class WithParts(
    Generic[TParentClass, TBuilderOutput, TBuilderPart],
    ABC,
):
    parts: list[TBuilderPart] = []

    def add(
        self,
        part: TBuilderPart,
    ) -> TParentClass:
        this = cast(TParentClass, self)

        self.parts.append(part)

        return this

    @abstractmethod
    def build_parts(
        self,
        *args: Any,
        **kwds: Any,
    ) -> TBuilderOutput:
        pass
