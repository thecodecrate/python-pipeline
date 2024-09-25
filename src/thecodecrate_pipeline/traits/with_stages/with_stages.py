from abc import ABC
from typing import Generic
from .parent_class import TParentClass
from .stage_interface import StageInterface, StageOrCallable
from ...core.pipeline.payload import TPayload


class WithStages(
    StageInterface[TPayload],
    Generic[TParentClass, TPayload],
    ABC,
):
    def __call__(
        self: TParentClass,  # type: ignore
        payload: TPayload,
    ) -> TPayload:
        return self.build_parts(payload)

    def pipe(
        self: TParentClass,  # type: ignore
        stage: StageOrCallable[TPayload],
    ) -> TParentClass:
        return self.add(stage)
