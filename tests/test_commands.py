import pytest
from thecodecrate_pipeline import (
    Pipeline,
    ChainedProcessor,
    Command,
    CommandProcessingStrategy,
    Processor,
    ProcessableAsCommand,
    ProcessorProcessingStrategy,
)


@pytest.mark.asyncio
async def test_custom_command_class():
    class MyCommand(Command[int, int]):
        async def execute(self) -> int:
            for stage in self.stages:
                self.payload = await self._call_stage(
                    payload=self.payload,
                    stage=stage,
                    *self.extra_args,
                    **self.extra_kwds,
                )

            return self.payload * 10

    class MyProcessor(Processor[int, int]):
        command_class = MyCommand

    class MyPipeline(Pipeline[int, int]):
        processor_class = MyProcessor

    pipeline = (
        MyPipeline()
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload * 3)
    )

    assert await pipeline.process(5) == 360


@pytest.mark.asyncio
async def test_trait_processable_as_command():
    class MyCommand(Command[int, int]):
        async def execute(self) -> int:
            for stage in self.stages:
                self.payload = await self._call_stage(
                    payload=self.payload,
                    stage=stage,
                )

            return self.payload * 5

    class MyProcessor(Processor[int, int]):
        command_class = MyCommand

    class MyPipeline(
        Pipeline[int, int],
        ProcessableAsCommand,
    ):
        processor_class = MyProcessor

    pipeline = (
        MyPipeline()
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload * 3)
    )

    assert await pipeline.process(5) == 180


@pytest.mark.asyncio
async def test_set_processor_and_strategy_on_pipeline_constructor():
    class TimesTenCommand(Command[int, int]):
        async def execute(self) -> int:
            for stage in self.stages:
                self.payload = await self._call_stage(
                    payload=self.payload,
                    stage=stage,
                )

            return self.payload * 5

    class MyProcessor(ChainedProcessor[int, int]):
        command_class = TimesTenCommand

    pipeline = (
        Pipeline(
            processor=MyProcessor(
                processing_strategy=CommandProcessingStrategy
            )
        )
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload * 3)
    )
    assert await pipeline.process(5) == 180

    pipeline = (
        Pipeline(
            processor=MyProcessor(
                processing_strategy=ProcessorProcessingStrategy
            )
        )
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload * 3)
    )
    assert await pipeline.process(5) == 36


@pytest.mark.asyncio
async def test_chained_processor_as_command():
    processor = ChainedProcessor[int](
        processing_strategy=CommandProcessingStrategy
    )

    result = await processor.process_with_strategy(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
    )
    assert result == 12

    processor = processor.with_processing_strategy_class(
        ProcessorProcessingStrategy
    )

    result = await processor.process_with_strategy(
        payload=5,
        stages=[
            lambda payload: payload + 1,
        ],
    )
    assert result == 6


@pytest.mark.asyncio
async def test_immutability_of_process_with_strategy():
    # define a command class
    class TimesTenCommand(Command[int, int]):
        async def execute(self) -> int:
            for stage in self.stages:
                self.payload = await self._call_stage(
                    payload=self.payload,
                    stage=stage,
                )

            return self.payload * 10

    class MyProcessor(ChainedProcessor[int, int]):
        command_class = TimesTenCommand

    # test "command" processing strategy
    processor_as_command = MyProcessor(
        processing_strategy=CommandProcessingStrategy
    )

    result = await processor_as_command.process_with_strategy(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
    )
    assert result == 120

    # change the processing strategy to "processor"
    processor = processor_as_command.with_processing_strategy_class(
        ProcessorProcessingStrategy
    )

    result = await processor.process_with_strategy(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
    )
    assert result == 12


@pytest.mark.asyncio
async def test_command_with_extra_arguments():
    # define a command class
    class MultiplyCommand(Command[int, int]):
        async def execute(self, factor: int) -> int:
            for stage in self.stages:
                self.payload = await self._call_stage(
                    payload=self.payload,
                    stage=stage,
                )

            return self.payload * factor

    class MyProcessor(ChainedProcessor[int, int]):
        command_class = MultiplyCommand

    # test command
    processor = MyProcessor()

    result = await processor.process_with_strategy(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
        factor=8,
    )
    assert result == 96
