import pytest

from thecodecrate_pipeline import Pipeline
from thecodecrate_pipeline.processors import (
    ChainedPipeline,
    ChainedProcessor,
    InterruptiblePipeline,
    InterruptibleProcessor,
)

from .stubs.stub_processor import StubProcessor


@pytest.mark.asyncio
async def test_custom_processor():
    processor = StubProcessor()

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert await pipeline.process(1) == 30

    assert pipeline.processor_instance.__class__ == StubProcessor


@pytest.mark.asyncio
async def test_chained_pipeline():
    pipeline = (
        ChainedPipeline[int]()
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
    )
    assert await pipeline.process(5) == 12

    assert pipeline.processor_instance.__class__ == ChainedProcessor


@pytest.mark.asyncio
async def test_chained_processor():
    processor = ChainedProcessor[int]()

    result = await processor.process(
        payload=5,
        stages=(
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ),
    )
    assert result == 12

    result = await processor.process(
        payload=5,
        stages=(lambda payload: payload + 1,),
    )
    assert result == 6


@pytest.mark.asyncio
async def test_pipeline_with_chained_processor():
    processor = ChainedProcessor[int]()

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload + 2)
        .pipe(lambda payload: payload * 5)
        .pipe(lambda payload: payload * 10)
    )

    assert await pipeline.process(5) == 350
    assert await pipeline.process(1) == 150

    assert pipeline.processor_instance.__class__ == ChainedProcessor


@pytest.mark.asyncio
async def test_interruptible_pipeline():
    pipeline = (
        InterruptiblePipeline[int](lambda payload: payload >= 10)
        .pipe(lambda payload: payload + 2)
        .pipe(lambda payload: payload * 10)
        .pipe(lambda payload: payload * 10)
    )

    assert await pipeline.process(5) == 70

    assert pipeline.processor_instance.__class__ == InterruptibleProcessor


@pytest.mark.asyncio
async def test_interruptible_processor():
    processor = InterruptibleProcessor[int](lambda payload: payload >= 10)

    result = await processor.process(
        payload=5,
        stages=(
            lambda payload: payload + 2,
            lambda payload: payload * 10,
            lambda payload: payload * 10,
        ),
    )
    assert result == 70

    result = await processor.process(
        payload=5,
        stages=(lambda payload: payload + 2,),
    )
    assert result == 7


@pytest.mark.asyncio
async def test_pipeline_with_interruptible_processor():
    processor = InterruptibleProcessor[int](lambda payload: payload >= 20)

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload + 2)
        .pipe(lambda payload: payload * 5)
        .pipe(lambda payload: payload * 10)
    )

    assert await pipeline.process(5) == 35
    assert await pipeline.process(1) == 150

    assert pipeline.processor_instance.__class__ == InterruptibleProcessor
