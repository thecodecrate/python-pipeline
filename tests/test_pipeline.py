import pytest

from thecodecrate_pipeline import Pipeline
from thecodecrate_pipeline.types import StageCollection, StageInstanceCollection

from .stubs.stub_processor import StubProcessor
from .stubs.stub_stage import StubStage
from .stubs.stub_stage_with_custom_args import (
    IndexedPipeline,
    IndexedProcessor,
    IndexedStage,
)
from .stubs.stub_stages_int import (
    AddOneStage,
    TimesThreeStage,
    TimesTwoStage,
)


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
async def test_pipelinebased_stages():
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
async def test_stages_with_different_types():
    pipeline = (
        (Pipeline[int, str]())
        .pipe(lambda x: x + 1)
        .pipe(lambda payload: f"total is {payload}!")
    )

    assert await pipeline.process(10) == "total is 11!"


@pytest.mark.asyncio
async def test_process_repeat():
    # it happened before that the pipeline was not reset,
    # making the second process call would not work as expected.
    for _ in range(3):
        pipeline = (
            (Pipeline[int]())
            .pipe(lambda payload: payload + 1)
            .pipe(lambda payload: payload * 2)
            .pipe(lambda payload: payload + 1)
        )

        for __ in range(3):
            assert await pipeline.process(1) == 5
            assert await pipeline.process(2) == 7


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
async def test_declarative_stages():
    pipeline = (Pipeline[int]()).pipe(TimesTwoStage()).pipe(AddOneStage())

    def add_seven(payload: int) -> int:
        return payload + 7

    async def sub_three_async(payload: int) -> int:
        return payload - 3

    class MyPipeline(Pipeline[int]):
        stages = (
            TimesThreeStage(),  # stage instance
            pipeline,  # pipeline
            AddOneStage,  # stage class
            add_seven,  # function
            sub_three_async,  # async function
        )

    assert await MyPipeline().process(5) == 36


@pytest.mark.asyncio
async def test_declarative_stages_with_processor():
    class MyPipeline(Pipeline[int]):
        processor_class = StubProcessor
        stages = (
            TimesTwoStage,
            TimesThreeStage,
        )

    pipeline = MyPipeline()

    assert await pipeline.process(5) == 300

    assert pipeline.__class__ == MyPipeline
    assert pipeline.processor_instance.__class__ == StubProcessor


@pytest.mark.asyncio
async def test_declarative_stage_instances():
    pipeline = (Pipeline[int]()).pipe(TimesTwoStage()).pipe(AddOneStage())

    def add_seven(payload: int) -> int:
        return payload + 7

    async def sub_three_async(payload: int) -> int:
        return payload - 3

    class MyPipeline(Pipeline[int]):
        stage_instances = (
            TimesThreeStage(),  # stage instance
            pipeline,  # pipeline
            AddOneStage(),  # another stage instance
            add_seven,  # function
            sub_three_async,  # async function
        )

    stage_instances: StageInstanceCollection = (
        add_seven,  # function
        sub_three_async,  # async function
    )

    assert await MyPipeline().process(5) == 36
    assert await MyPipeline(stage_instances=stage_instances).process(5) == 9


@pytest.mark.asyncio
async def test_declarative_stage_instances__immutability():
    def add_seven(payload: int) -> int:
        return payload + 7

    async def sub_three_async(payload: int) -> int:
        return payload - 3

    stage_instances: StageInstanceCollection = (
        add_seven,  # function
        sub_three_async,  # async function
    )

    pipeline = Pipeline(stage_instances=stage_instances)

    assert await pipeline.process(5) == 9

    # adding more stages should not affect the original pipeline
    stage_instances += (TimesTwoStage(),)

    assert await pipeline.process(5) == 9


@pytest.mark.asyncio
async def test_constructor_override_declared_stages():
    class MyPipeline(Pipeline[int]):
        stages = (
            TimesTwoStage,  # stage class
            TimesThreeStage(),  # stage instance
        )

    stages: StageCollection = (
        AddOneStage,  # stage class
        TimesTwoStage(),  # stage instance
    )

    stage_instances: StageInstanceCollection = (
        AddOneStage(),  # only instances can be added
        TimesTwoStage(),  # only instances can be added
    )

    assert await MyPipeline().process(5) == 30
    assert await MyPipeline(stages=stages).process(5) == 12
    assert await MyPipeline(stages=stage_instances).process(5) == 12
    assert await MyPipeline(stage_instances=stage_instances).process(5) == 12


@pytest.mark.asyncio
async def test_custom_args_on_stages():
    class MyIndexedStage(IndexedStage[str]):
        async def __call__(self, payload: str, index: int) -> str:
            return f"{payload}: {index}"

    pipeline = (IndexedPipeline[str]()).pipe(MyIndexedStage()).pipe(MyIndexedStage())

    assert await pipeline.process("test") == "test: 0: 1"
    assert pipeline.processor_instance.__class__ == IndexedProcessor
    assert pipeline.__class__ == IndexedPipeline


@pytest.mark.asyncio
async def test_method__with_stages():
    pipeline = Pipeline()

    stages: StageCollection = (
        AddOneStage,  # stage class
        TimesTwoStage(),  # stage instance
    )

    new_pipeline = pipeline.with_stages(stages)

    assert new_pipeline is not pipeline  # ensures immutability
    assert len(new_pipeline.stages) == len(stages)
    for stage in stages:
        assert stage in new_pipeline.stages


@pytest.mark.asyncio
async def test_method__with_stages__override_current_instances():
    pipeline = Pipeline().pipe(AddOneStage())

    stages: StageCollection = (
        TimesTwoStage,  # stage class
        TimesThreeStage(),  # stage instance
    )

    new_pipeline = pipeline.with_stages(stages)

    assert len(pipeline.stage_instances) == 1
    assert len(new_pipeline.stage_instances) == 2

    assert await pipeline.process(5) == 6
    assert await new_pipeline.process(5) == 30
