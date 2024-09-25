from abc import ABC
from typing import Any, Generic, TypeVar
from ...traits.with_parts.with_parts import WithParts
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class ParentClass(
    WithParts[Any, TBuilderOutput, TBuilderPart],
    Generic[TBuilderOutput, TBuilderPart],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any, Any])
