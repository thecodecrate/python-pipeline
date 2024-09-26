from abc import ABC
from typing import Generic

from .parent_class import TParentClass
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload


class WithStages(
    Generic[TParentClass, TPayload],
    ABC,
):
    stages: list[PipelineCallable[TPayload]] = []

    def get_parts(self) -> list[PipelineCallable[TPayload]]:
        return self.stages

    def set_parts(self, parts: list[PipelineCallable[TPayload]]) -> None:
        self.stages = parts
