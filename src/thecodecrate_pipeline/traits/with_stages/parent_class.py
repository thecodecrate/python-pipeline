from abc import ABC
from typing import Any, Generic, TypeVar
from .stage_interface import StageOrCallable
from ...core.pipeline.payload import TPayload
from ...support.libraries.builderable import Builderable


class ParentClass(
    Builderable[TPayload, StageOrCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any])
