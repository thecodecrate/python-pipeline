from abc import ABC
from typing import Any, Generic, TypeVar

from ..with_stages.with_stages import WithStages
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload
from ...support.libraries.builderable import Builderable


class ParentClass(
    WithStages[Any, TPayload],
    Builderable[TPayload, PipelineCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass


TParentClass = TypeVar("TParentClass", bound=ParentClass[Any])
