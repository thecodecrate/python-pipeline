import pytest

from thecodecrate_pipeline import (
    PipelineBuilder,
)
from .stubs.stub_stages_int import (
    AddOneStage,
    TimesThreeStage,
    TimesTwoStage,
)


@pytest.mark.asyncio
async def test_pipeline_builder():
    pipeline_builder = (
        (PipelineBuilder[int]())
        .add(AddOneStage())
        .add(TimesTwoStage())
        .add(lambda payload: payload + 1)
        .add(AddOneStage())
    )

    pipeline = pipeline_builder.build()

    assert await pipeline.process(1) == 6


@pytest.mark.asyncio
async def test_immutability():
    pipeline_builder = (
        (PipelineBuilder[int]())
        .add(AddOneStage())
        .add(TimesTwoStage())
        .add(AddOneStage())
    )

    pipeline = pipeline_builder.build()

    assert await pipeline.process(1) == 5

    new_builder = pipeline_builder.add(TimesThreeStage())
    new_pipeline = new_builder.build()

    assert await new_pipeline.process(1) == 15
    assert await pipeline.process(1) == 5
