import pytest

from tests.stubs.stub_stage_with_custom_args import (
    IndexedPipeline,
    IndexedStage,
)
from thecodecrate_pipeline import (
    Pipeline,
    InterruptibleProcessor,
)
from .stubs.stub_stages_int import (
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

    assert await pipeline.process(1) == 5
    assert await pipeline.process(2) == 7


@pytest.mark.asyncio
async def test_classbased_stages():
    pipeline = (
        (Pipeline[int]())
        .pipe(TimesTwoStage())
        .pipe(AddOneStage())
        .pipe(TimesThreeStage())
    )

    assert await pipeline.process(5) == 33


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

    assert await pipeline.process(10) == 736


@pytest.mark.asyncio
async def test_string_stage():
    pipeline = (Pipeline[str]()).pipe(StubStage())

    assert await pipeline.process("") == "stubbed response"


@pytest.mark.asyncio
async def test_pipeline_immutability():
    pipeline = (
        (Pipeline[int]())
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert await pipeline.process(1) == 3

    pipeline2 = pipeline.pipe(lambda payload: payload + 1)

    assert await pipeline.process(1) == 3
    assert await pipeline2.process(1) == 4


@pytest.mark.asyncio
async def test_custom_processor():
    processor = StubProcessor()

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload + 1)
        .pipe(lambda payload: payload + 1)
    )

    assert await pipeline.process(1) == 30


@pytest.mark.asyncio
async def test_interruptible_processor():
    processor = InterruptibleProcessor[int](lambda payload: payload > 5)

    pipeline = (
        (Pipeline[int](processor=processor))
        .pipe(lambda payload: payload * 2)
        .pipe(lambda payload: payload + 1)
    )

    assert await pipeline.process(3) == 7
    assert await pipeline.process(1) == 2


@pytest.mark.asyncio
async def test_declarative_stages():
    pipeline = (Pipeline[int]()).pipe(TimesTwoStage()).pipe(AddOneStage())

    def add_seven(payload: int) -> int:
        return payload + 7

    async def sub_three_async(payload: int) -> int:
        return payload - 3

    class MyPipeline(Pipeline[int]):
        stages = [
            TimesThreeStage(),  # stage instance
            pipeline,  # pipeline
            AddOneStage,  # stage class
            add_seven,  # function
            sub_three_async,  # async function
        ]

    assert await MyPipeline().process(5) == 36


@pytest.mark.asyncio
async def test_declarative_stages_with_processor():
    class MyPipeline(Pipeline[int]):
        processor_class = StubProcessor
        stages = [
            TimesTwoStage,
            TimesThreeStage,
        ]

    assert await MyPipeline().process(5) == 300


@pytest.mark.asyncio
async def test_stages_with_custom_args():
    class MyIndexedStage(IndexedStage[str]):
        async def __call__(self, payload: str, index: int) -> str:
            return f"{payload}: {index}"

    pipeline = (
        (IndexedPipeline[str]()).pipe(MyIndexedStage()).pipe(MyIndexedStage())
    )

    assert await pipeline.process("test") == "test: 0: 1"
