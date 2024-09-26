from abc import ABC
from typing import Generic, Optional, cast

from .parent_class import TParentClass
from ..with_processor.processor_interface import ProcessorInterface
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline import Pipeline


class WithPipelineBuilder(
    Generic[TParentClass, TPayload],
    ABC,
):
    def add(
        self,
        part: PipelineCallable[TPayload],
    ) -> TParentClass:
        parent = cast(TParentClass, super())

        return parent.add(part)

    def build_parts(
        self: TParentClass,  # type: ignore
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> Pipeline[TPayload]:
        return Pipeline[TPayload](processor=processor, stages=self.stages)

    def build(
        self: TParentClass,  # type: ignore
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> Pipeline[TPayload]:
        return self.build_parts(processor)
