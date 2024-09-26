import pytest

from thecodecrate_pipeline import (
    PipelineBuilder,
)
from .stubs.stub_int_stages import (
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

    assert pipeline.process(1) == 6


@pytest.mark.asyncio
async def test_immutability():
    pipeline_builder = (
        (PipelineBuilder[int]())
        .add(AddOneStage())
        .add(TimesTwoStage())
        .add(AddOneStage())
    )

    pipeline = pipeline_builder.build()

    assert pipeline.process(1) == 5

    new_builder = pipeline_builder.add(TimesThreeStage())

    assert new_builder.build().process(1) == 15

    assert pipeline.process(1) == 5
