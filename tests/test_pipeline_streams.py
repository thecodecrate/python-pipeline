import pytest
import asyncio
from typing import AsyncIterator

from thecodecrate_pipeline import Pipeline


# Define the stages
async def stage1(stream: AsyncIterator[int]) -> AsyncIterator[int]:
    async for item in stream:
        # Multiply each item by 2
        yield item * 2
        await asyncio.sleep(0.1)  # Simulate processing delay


async def stage2(stream: AsyncIterator[int]) -> AsyncIterator[str]:
    async for item in stream:
        # Convert each item to a formatted string
        yield f"Number: {item}"
        await asyncio.sleep(0.1)


# Create the pipeline
pipeline = (
    Pipeline[AsyncIterator[int], AsyncIterator[str]]()
    .pipe(stage1)
    .pipe(stage2)
)


# Define the input stream
async def input_stream() -> AsyncIterator[int]:
    for i in range(5):
        yield i
        await asyncio.sleep(0.1)


@pytest.mark.asyncio
async def test_pipeline_streams():
    # Process the input stream through the pipeline
    stream = await pipeline.process(input_stream())

    # Collect the results
    results: list[str] = []
    async for result in stream:
        results.append(result)

    # Assert that the results are as expected
    assert results == [
        "Number: 0",
        "Number: 2",
        "Number: 4",
        "Number: 6",
        "Number: 8",
    ]
