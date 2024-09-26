from abc import ABC
from typing import Generic

from .parent_class import TParentClass
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline_callable import PipelineCallable


class WithPipe(
    Generic[TParentClass, TPayload],
    ABC,
):
    def pipe(
        self: TParentClass,  # type: ignore
        stage: PipelineCallable[TPayload],
    ) -> TParentClass:
        return self.add(stage)
