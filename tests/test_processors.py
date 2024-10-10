import pytest
from thecodecrate_pipeline import (
    ChainedPipeline,
    ChainedProcessor,
    InterruptiblePipeline,
    InterruptibleProcessor,
    StatefulChainedPipeline,
    StatefulChainedProcessor,
)


@pytest.mark.asyncio
async def test_chained_pipeline():
    pipeline = (
        ChainedPipeline[int]()
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
    )
    assert await pipeline.process(5) == 12


@pytest.mark.asyncio
async def test_chained_processor():
    processor = ChainedProcessor[int]()

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
    )
    assert result == 12

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 1,
        ],
    )
    assert result == 6


@pytest.mark.asyncio
async def test_interruptible_pipeline():
    pipeline = (
        InterruptiblePipeline[int](lambda payload: payload < 10)
        .pipe(lambda payload: payload + 2)
        .pipe(lambda payload: payload * 10)
        .pipe(lambda payload: payload * 10)
    )
    assert await pipeline.process(5) == 70


@pytest.mark.asyncio
async def test_interruptible_processor():
    processor = InterruptibleProcessor[int](lambda payload: payload < 10)

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 2,
            lambda payload: payload * 10,
            lambda payload: payload * 10,
        ],
    )
    assert result == 70

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 2,
        ],
    )
    assert result == 7


@pytest.mark.asyncio
async def test_stateful_chained_pipeline():
    pipeline = (
        StatefulChainedPipeline[int]()
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
    )
    assert await pipeline.process(5) == 12


@pytest.mark.asyncio
async def test_stateful_chained_processor():
    processor = StatefulChainedProcessor[int]()

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 1,
            lambda payload: payload * 2,
        ],
    )
    assert result == 12

    result = await processor.process(
        payload=5,
        stages=[
            lambda payload: payload + 1,
        ],
    )
    assert result == 6
