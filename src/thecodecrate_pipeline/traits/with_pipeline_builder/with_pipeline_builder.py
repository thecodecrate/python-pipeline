from typing import Generic, Optional, Protocol, Self

from ..with_builderable.with_builderable import WithBuilderable
from ..with_processor.with_processor import WithProcessor
from ..with_stages.with_stages import WithStages
from ..with_processor.processor_interface import ProcessorInterface
from ...core.pipeline.pipeline_callable import PipelineCallable
from ...core.pipeline.payload import TPayload
from ...core.pipeline.pipeline import Pipeline


class WithPipelineBuilder(
    WithProcessor[TPayload],
    WithStages[TPayload],
    WithBuilderable[TPayload],
    Generic[TPayload],
    Protocol,
):
    def add(self, part: PipelineCallable[TPayload]) -> Self:
        return self.add_part(part)

    def build(
        self,
        processor: Optional[ProcessorInterface[TPayload]] = None,
    ) -> Pipeline[TPayload]:
        return Pipeline[TPayload](processor=processor, stages=self.get_parts())
