from abc import ABC
from typing import Any, Generic, TypeVar
from thecodecrate_builderable import Builderable

from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload


class ParentClass(
    Builderable[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any])
