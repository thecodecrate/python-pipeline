import pytest

from thecodecrate_pipeline import (
    Pipeline,
    InterruptibleProcessor,
)
from .stubs.stub_int_stages import (
    AddOneStage,
    TimesThreeStage,
    TimesTwoStage,
)
from .stubs.stub_stage import StubStage
from .stubs.stub_processor import StubProcessor


@pytest.mark.asyncio
async def test_lambda_stages():
    pipeline = (
        (Pipeline[int]())
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload + 1)
    )

    assert pipeline.process(1) == 5
    assert pipeline.process(2) == 7


@pytest.mark.asyncio
async def test_classbased_stages():
    pipeline = (
        (Pipeline[int]())
        .pipe(TimesTwoStage())
        .pipe(AddOneStage())
        .pipe(TimesThreeStage())
    )

    assert pipeline.process(5) == 33


@pytest.mark.asyncio
async def test_pipeline_stages():
    sub_pipeline1 = (
        (Pipeline[int]())
        .pipe(TimesTwoStage())
        .pipe(AddOneStage())
        .pipe(TimesThreeStage())
    )

    sub_pipeline2 = (
        (Pipeline[int]())
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload * 2)
    )

    pipeline = (
        (Pipeline[int]())
        .pipe(TimesThreeStage())
        .pipe(sub_pipeline1)
        .pipe(sub_pipeline2)
        .pipe(lambda payload: payload * 2)
    )

    assert pipeline.process(10) == 736


@pytest.mark.asyncio
async def test_string_stage():
    pipeline = (Pipeline[str]()).pipe(StubStage())

    assert pipeline.process("") == "stubbed response"


@pytest.mark.asyncio
async def test_pipeline_immutability():
    pipeline = (
        (Pipeline[int]())
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert pipeline.process(1) == 3

    pipeline2 = pipeline.pipe(lambda payload: payload + 1)

    assert pipeline.process(1) == 3

    assert pipeline2.process(1) == 4


@pytest.mark.asyncio
async def test_custom_processor():
    processor = StubProcessor()

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert pipeline.process(1) == 30


@pytest.mark.asyncio
async def test_interruptible_processor():
    processor = InterruptibleProcessor[int](lambda payload: payload > 5)

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload + 1)
    )

    assert pipeline.process(3) == 7

    assert pipeline.process(1) == 2
