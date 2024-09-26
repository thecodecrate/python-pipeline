from abc import ABC, abstractmethod
from typing import Generic, Any, cast
from .parent_class import TParentClass
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class WithParts(
    Generic[TParentClass, TBuilderOutput, TBuilderPart],
    ABC,
):
    _parts: list[TBuilderPart] = []

    def get_parts(self) -> list[TBuilderPart]:
        return self._parts

    def set_parts(self, parts: list[TBuilderPart]) -> None:
        self._parts = parts

    def add(
        self,
        part: TBuilderPart,
    ) -> TParentClass:
        self.get_parts().append(part)

        return cast(TParentClass, self)

    @abstractmethod
    def build_parts(
        self,
        *args: Any,
        **kwds: Any,
    ) -> TBuilderOutput:
        pass
