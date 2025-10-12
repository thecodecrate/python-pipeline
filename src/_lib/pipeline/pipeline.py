from typing import Any, Optional, Self

from .callable_type import CallableCollection, CallableType, StageDefinitionCollection
from .pipeline_interface import PipelineInterface as ImplementsInterface
from .processor_interface import ProcessorInterface
from .processors.chained_processor import ChainedProcessor
from .traits.clonable import Clonable
from .types import T_in, T_out


class Pipeline(
    Clonable,
    ImplementsInterface[T_in, T_out],
):
    stages: StageDefinitionCollection
    stage_instances: CallableCollection
    processor: Optional[type[ProcessorInterface] | ProcessorInterface]
    processor_instance: Optional[ProcessorInterface]

    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        stage_instances: Optional[CallableCollection] = None,
        processor: Optional[type[ProcessorInterface] | ProcessorInterface] = None,
        processor_instance: Optional[ProcessorInterface] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "stage_instances"):
            self.stage_instances = tuple()

        if not hasattr(self, "processor"):
            self.processor = self._get_default_processor()

        if not hasattr(self, "processor_instance"):
            self.processor_instance = None

        if stages:
            self.stages = stages

        if stage_instances:
            self.stage_instances = stage_instances

        if self._should_instantiate_stages():
            self._instantiate_stages()

        if processor:
            self.processor = processor

        if processor_instance:
            self.processor_instance = processor_instance

        if self._should_instantiate_processor():
            self._instantiate_processor()

    async def process(self, payload: T_in, *args: Any, **kwds: Any) -> T_out:
        """
        Process the given payload through the pipeline.
        """
        if self.processor_instance is None:
            raise ValueError("Processor not set")

        return await self.processor_instance.process(
            payload=payload, stages=self.stage_instances, *args, **kwds
        )

    def pipe(self, stage: CallableType) -> Self:
        """
        Adds a single stage to the pipeline.
        """
        return self.clone({"stage_instances": tuple([*self.stage_instances, stage])})

    async def __call__(
        self,
        payload: T_in,
        /,  # Make 'payload' a positional-only parameter
        *args: Any,
        **kwds: Any,
    ) -> T_out:
        """
        Processes payload through the pipeline.
        """
        return await self.process(payload, *args, **kwds)

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self:
        """
        Attachs a processor (class or instance) to the pipeline.
        """
        cloned = self.clone({"processor": processor, "processor_instance": None})

        return cloned._instantiate_processor()

    def with_stages(self, stages: StageDefinitionCollection) -> Self:
        """
        Adds a collection of stages to the pipeline.
        """
        cloned = self.clone({"stages": stages, "stage_instances": []})

        return cloned._instantiate_stages()

    def get_processor_instance(self) -> Optional[ProcessorInterface]:
        return self.processor_instance

    def get_stages(self) -> StageDefinitionCollection:
        return self.stages

    def _get_default_processor(self) -> type[ChainedProcessor[T_in, T_out]]:
        return ChainedProcessor

    def _should_instantiate_processor(self) -> bool:
        return self.processor_instance is None

    def _instantiate_processor(self) -> Self:
        if self.processor is None:
            raise ValueError("Processor class not set")

        if isinstance(self.processor, type):
            self.processor_instance = self.processor()
        else:
            self.processor_instance = self.processor

        if isinstance(self.processor_instance, type):
            raise ValueError("Processor instance could not be created")

        return self

    def _should_instantiate_stages(self) -> bool:
        return len(self.stage_instances) == 0 and len(self.stages) > 0

    def _instantiate_stages(self) -> Self:
        self.stage_instances = tuple(
            stage() if isinstance(stage, type) else stage for stage in self.stages
        )

        return self
