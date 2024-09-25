from abc import ABC
from typing import Any, Generic, TypeVar
from ...core.builderable.types import TBuilderPart, TBuilderOutput


class ParentClass(
    Generic[TBuilderOutput, TBuilderPart],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any, Any])
