import pytest

from src.thecodecrate_pipeline.core.pipeline.pipeline import Pipeline


@pytest.mark.asyncio
async def test_basic_instructions():
    pipeline = (
        (Pipeline[int]())
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert pipeline.process(1) == 3
