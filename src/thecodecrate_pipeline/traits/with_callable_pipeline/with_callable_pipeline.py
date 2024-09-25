from abc import ABC
from typing import Generic

from .parent_class import TParentClass
from ..with_stages.stage_interface import StageInterface
from ...core.pipeline.payload import TPayload


class WithCallablePipeline(
    StageInterface[TPayload],
    Generic[TParentClass, TPayload],
    ABC,
):
    def __call__(
        self: TParentClass,  # type: ignore
        payload: TPayload,
    ) -> TPayload:
        return self.build_parts(payload)
