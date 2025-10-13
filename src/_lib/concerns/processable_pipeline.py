from abc import ABC
from typing import Any, Optional, Self

from ..contracts.processable_pipeline import ProcessablePipeline as ImplementsInterface
from ..contracts.processor import Processor as ProcessorContract
from ..processors.chained_processor.chained_processor import ChainedProcessor
from ..types.types import T_in, T_out


class ProcessablePipeline(
    ImplementsInterface[T_in, T_out],
    ABC,
):
    processor: Optional[type[ProcessorContract] | ProcessorContract]
    processor_instance: Optional[ProcessorContract]

    def __init__(
        self,
        processor: Optional[type[ProcessorContract] | ProcessorContract] = None,
        processor_instance: Optional[ProcessorContract] = None,
        *args: Any,
        **kwds: Any,
    ) -> None:
        super().__init__(*args, **kwds)  # type: ignore

        if not hasattr(self, "processor"):
            self.processor = self._get_default_processor()

        if not hasattr(self, "processor_instance"):
            self.processor_instance = None

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
            payload=payload, stages=self.get_stages_instances(), *args, **kwds
        )

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
        self, processor: type[ProcessorContract] | ProcessorContract
    ) -> Self:
        """
        Attachs a processor (class or instance) to the pipeline.
        """
        cloned = self.clone({"processor": processor, "processor_instance": None})

        return cloned._instantiate_processor()

    def get_processor_instance(self) -> Optional[ProcessorContract]:
        return self.processor_instance

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
