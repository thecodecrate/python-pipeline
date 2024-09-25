from abc import ABC
from typing import Any, Generic, TypeVar
from ...core.pipeline.payload import TPayload
from ...traits.with_stages.stage_interface import StageOrCallable
from ...traits.with_stages.with_stages import WithStages
from ...support.libraries.builderable import Builderable


class ParentClass(
    WithStages[Any, TPayload],
    Builderable[TPayload, StageOrCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any])
