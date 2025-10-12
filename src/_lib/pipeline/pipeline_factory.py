from typing import Any, Optional, Self

from .callable_type import StageDefinition, StageDefinitionCollection
from .pipeline import Pipeline
from .pipeline_factory_interface import PipelineFactoryInterface as ImplementsInterface
from .pipeline_interface import PipelineInterface
from .processor_interface import ProcessorInterface
from .traits.act_as_factory.act_as_factory import ActAsFactory
from .types import T_in, T_out


class PipelineFactory(
    ActAsFactory[PipelineInterface[T_in, T_out]],
    ImplementsInterface[T_in, T_out],
):
    stages: StageDefinitionCollection
    processor: Optional[type[ProcessorInterface[T_in, T_out]] | ProcessorInterface]
    pipeline_class: Optional[type[PipelineInterface[T_in, T_out]]]

    def __init__(
        self,
        stages: Optional[StageDefinitionCollection] = None,
        processor: Optional[type[ProcessorInterface] | ProcessorInterface] = None,
        pipeline_class: Optional[type[PipelineInterface[T_in, T_out]]] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        if not hasattr(self, "stages"):
            self.stages = tuple()

        if not hasattr(self, "processor"):
            self.processor = None

        if not hasattr(self, "pipeline_class"):
            self.pipeline_class = self._get_default_pipeline_class()

        if stages:
            self.stages = stages

        if processor:
            self.with_processor(processor)

        if pipeline_class:
            self.pipeline_class = pipeline_class

    def add_stage(self, stage: StageDefinition) -> Self:
        """
        Adds a single stage to the pipeline.
        """
        self.stages = self.stages + (stage,)

        return self

    def with_stages(self, stages: StageDefinitionCollection) -> Self:
        """
        Adds a collection of stages to the pipeline.
        """
        self.stages = stages

        return self

    def with_processor(
        self, processor: type[ProcessorInterface] | ProcessorInterface
    ) -> Self:
        """
        Attachs a processor (class or instance) to the pipeline factory.
        """
        self.processor = processor

        return self

    def _get_default_pipeline_class(
        self,
    ) -> Optional[type[PipelineInterface[T_in, T_out]]]:
        return Pipeline

    # ActAsFactory
    def _definition(self) -> dict[str, Any]:
        return {
            "stages": self.stages,
            "processor": self.processor,
        }

    # ActAsFactory
    def _get_target_class(self) -> type[PipelineInterface[T_in, T_out]]:
        if self.pipeline_class is None:
            raise ValueError("Pipeline class not set in factory.")

        return self.pipeline_class
