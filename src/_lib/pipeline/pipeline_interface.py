from typing import Any, Optional, Protocol, Self, TypeVar

from .callable_type import CallableCollection, CallableType, StageDefinitionCollection
from .processor_interface import ProcessorInterface
from .traits.clonable import ClonableInterface
from .types import T_in, T_out


class PipelineInterface(
    ClonableInterface,
    Protocol[T_in, T_out],
):
    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        stage_instances: Optional[CallableCollection] = None,
        processor: Optional[type[ProcessorInterface] | ProcessorInterface] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        *args: Any,
        **kwds: Any,
    ) -> None: ...

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out: ...

    def pipe(self, stage: CallableType) -> Self: ...

    async def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out: ...

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self: ...

    def with_stages(self, stages: StageDefinitionCollection) -> Self: ...

    def get_processor_instance(self) -> Optional[ProcessorInterface]: ...

    def get_stages(self) -> StageDefinitionCollection: ...


TPipeline = TypeVar("TPipeline", bound=PipelineInterface, infer_variance=True)
