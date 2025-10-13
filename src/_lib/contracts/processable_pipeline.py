from typing import Any, Optional, Protocol, Self

from ..types.types import T_in, T_out
from .base_pipeline import BasePipeline as BasePipelineContract
from .processor import Processor as ProcessorContract
from .stageable_pipeline import StageablePipeline as StageablePipelineContract


class ProcessablePipeline(
    StageablePipelineContract[T_in, T_out],
    BasePipelineContract[T_in, T_out],
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        processor: Optional[type[ProcessorContract] | ProcessorContract] = None,
        processor_instance: Optional[ProcessorContract] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out: ...

    async def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    def with_processor(
        self, processor: type[ProcessorContract] | ProcessorContract
    ) -> Self: ...

    def get_processor_instance(self) -> Optional[ProcessorContract]: ...
