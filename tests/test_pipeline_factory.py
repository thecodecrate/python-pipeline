import pytest

from thecodecrate_pipeline import PipelineFactory, Stage
from thecodecrate_pipeline.processors import ChainedProcessor
from thecodecrate_pipeline.types import StageCollection

from .stubs.stub_stages_int import (
    AddOneStage,
)

some_stages: StageCollection = (
    AddOneStage,
    (lambda x: x + 1),
    (lambda x: f"result is {x}"),
)


@pytest.mark.asyncio
async def test_with_stages():
    pipeline_factory = (PipelineFactory[int, str]()).with_stages(some_stages)

    pipeline = pipeline_factory.make()

    assert await pipeline.process(10) == "result is 12"


@pytest.mark.asyncio
async def test_parameter_immutability():
    # creating a pipeline with a few stages
    pipeline_factory = (PipelineFactory()).with_stages(some_stages)
    pipeline = pipeline_factory.make()
    result = await pipeline.process(10)
    assert result == "result is 12"

    # let's try to change the stages list
    def add_excitement(x: str) -> str:
        return f"{x}!!!"

    pipeline_factory.add_stage(add_excitement)

    # the original "some_stages" list should not be affected
    result2 = await pipeline.process(10)
    assert result2 == result
    assert len(some_stages) == 3


@pytest.mark.asyncio
async def test_immutability():
    # creating a pipeline with a few stages
    pipeline_factory = (PipelineFactory[int, str]()).with_stages(some_stages)
    pipeline = pipeline_factory.make()
    result = await pipeline.process(10)
    assert result == "result is 12"

    # adding another stage after the pipeline has been created
    def add_excitement(x: str) -> str:
        return f"{x}!!!"

    pipeline_factory.add_stage(add_excitement)

    # the original pipeline is not affected
    result2 = await pipeline.process(10)
    assert result2 == result

    # now, let's create a new pipeline, with the excitement stage!!!
    pipeline2 = pipeline_factory.make()
    result3 = await pipeline2.process(10)

    # the new pipeline has the excitement!!!
    assert result3 == "result is 12!!!"

    # notice the original pipeline is not affected
    result4 = await pipeline.process(10)
    assert result4 == result

    # what if we try to change the original pipeline, directly?
    pipeline.pipe(
        add_excitement
    )  # <- adding the excitement stage to the original pipeline

    # the original pipeline is still not affected, due to the immutability
    # nature of pipelines
    result5 = await pipeline.process(10)
    assert result5 == result


@pytest.mark.asyncio
async def test_with_processor():
    class MyProcessor(ChainedProcessor):
        pass

    # create factory with a processor
    pipeline_factory = (
        (PipelineFactory[int, str]())
        .with_stages(some_stages)
        .with_processor(MyProcessor())
    )

    # create and process
    pipeline = pipeline_factory.make()
    result = await pipeline.process(10)
    assert result == "result is 12"

    # check the processor
    assert pipeline.get_processor_instance().__class__ == MyProcessor


@pytest.mark.asyncio
async def test_with_processor_class():
    class MyProcessor(ChainedProcessor):
        pass

    # create factory with a processor
    pipeline_factory = (
        (PipelineFactory[int, str]())
        .with_stages(some_stages)
        .with_processor_class(MyProcessor)
    )

    # create and process
    pipeline = pipeline_factory.make()
    result = await pipeline.process(10)
    assert result == "result is 12"

    # check the processor
    assert pipeline.get_processor_instance().__class__ == MyProcessor


@pytest.mark.asyncio
async def test_with_class_stages():
    class MyStage(Stage[int, str]):
        async def __call__(self, x: int) -> str:
            return f"result is {x}"

    pipeline_factory = (PipelineFactory[int, str]()).with_stages((MyStage,))

    pipeline = pipeline_factory.make()
    assert await pipeline.process(10) == "result is 10"


@pytest.mark.asyncio
async def test_with_declared_stages():
    class MyStage(Stage[int, str]):
        async def __call__(self, x: int) -> str:
            return f"result is {x}"

    class MyPipelineFactory(PipelineFactory[int, str]):
        stages = (MyStage,)

    pipeline_factory = MyPipelineFactory()

    pipeline = pipeline_factory.make()
    assert await pipeline.process(10) == "result is 10"
