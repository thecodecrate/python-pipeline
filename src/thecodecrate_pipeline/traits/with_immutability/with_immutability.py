from abc import ABC
from typing import Generic
from thecodecrate_builderable import (
    WithImmutability as BuilderableWithImmutability,
)

from .parent_class import TParentClass
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class WithImmutability(
    BuilderableWithImmutability[
        TParentClass,  # type: ignore
        TPayload,
        PipelineCallable[TPayload],
    ],
    Generic[TParentClass, TPayload],
    ABC,
):
    pass
