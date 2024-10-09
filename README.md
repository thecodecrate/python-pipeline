# TheCodeCrate's Pipeline

This package provides a pipeline pattern implementation.

The implementation is based on the excellent [PHP League Pipeline](https://github.com/thephpleague/pipeline) package.

## Installation

```bash
pip install thecodecrate-pipeline
```

## Pipeline Pattern

The pipeline pattern allows you to easily compose sequential stages by chaining stages.

In this particular implementation, the interface consists of two parts:

- `StageInterface`
- `PipelineInterface`

A pipeline consists of zero, one, or multiple stages. A pipeline can process a payload. During the processing, the payload will be passed to the first stage. From that moment on, the resulting value is passed on from stage to stage.

In the simplest form, the execution chain can be represented as a for loop:

```python
result = payload

for stage in stages:
    result = stage(result)

return result
```

Effectively, this is the same as:

```python
result = stage3(stage2(stage1(payload)))
```

## Immutability

Pipelines are implemented as immutable stage chains. When you pipe a new stage, a new pipeline will be created with the added stage. This makes pipelines easy to reuse and minimizes side-effects.

## Usage

Operations in a pipeline, stages, can be anything that satisfies the Callable type hint. So functions and anything that's callable is acceptable.

```python
pipeline = Pipeline().pipe(lambda payload: payload * 10)

# Returns 100
await pipeline.process(10)
```

## Class-Based Stages

Class-based stages are also possible. The `StageInterface[InputType, OutputType]` interface can be implemented, which ensures you have the correct method signature for the `__call__` method.

```python
class TimesTwoStage(StageInterface[int, int]):
    async def __call__(self, payload: int) -> int:
        return payload * 2

class AddOneStage(StageInterface[int, int]):
    async def __call__(self, payload: int) -> int:
        return payload + 1

pipeline = (
    Pipeline[int, int]()
    .pipe(TimesTwoStage())
    .pipe(AddOneStage())
)

# Returns 21
await pipeline.process(10)
```

## Reusable Pipelines

Because the `PipelineInterface` is an extension of the `StageInterface`, pipelines can be reused as stages. This creates a highly composable model to create complex execution patterns while keeping the cognitive load low.

For example, if we'd want to compose a pipeline to process API calls, we'd create something along these lines:

```python
process_api_request = (
    Pipeline()
    .pipe(ExecuteHttpRequest())
    .pipe(ParseJsonResponse())
)

pipeline = (
    Pipeline()
    .pipe(ConvertToPsr7Request())
    .pipe(process_api_request)
    .pipe(ConvertToResponseDto())
)

await pipeline.process(DeleteBlogPost(post_id))
```

## Type Hinting

You can specify the input and output types for pipelines and stages using type variables `T_in` and `T_out`. This allows you to handle varying types between stages, enhancing type safety and code clarity.

The `T_out` type variable is optional and defaults to `T_in`. Similarly, `T_in` is also optional and defaults to `Any`.

```python
from typing import Any

pipeline = Pipeline[int]().pipe(lambda payload: payload * 2)

# Returns 20
await pipeline.process(10)
```

You can also handle varying types between stages:

```python
pipeline = Pipeline[int, str]().pipe(lambda payload: f"Number: {payload}")

# Returns "Number: 10"
await pipeline.process(10)
```

This flexibility allows you to build pipelines that transform data types between stages seamlessly.

## Custom Processors

You can create your own processors to customize how the pipeline processes stages. This allows you to implement different execution strategies, such as handling exceptions, processing resources, or implementing middleware patterns.

For example, you can define a custom processor:

```python
class MyCustomProcessor(Processor[T_in, T_out]):
    async def process(
        self,
        payload: T_in,
        stages: list[StageInterface[T_in, T_out]],
        *args: Any,
        **kwargs: Any,
    ) -> T_out:
        # Custom processing logic
        result = payload
        for stage in stages:
            result = await stage(result)
        return result
```

And use it in your pipeline:

```python
pipeline = Pipeline[int, int](processor=MyCustomProcessor()).pipe(lambda x: x * 2)
```

## Declarative Stages

Instead of using `pipe` to add stages at runtime, you can define stages declaratively by specifying them as class-level attributes. This makes pipelines easier to set up and reuse with predefined stages.

```python
class MyPipeline(Pipeline[int, int]):
    stages = [
        TimesTwoStage(),
        TimesThreeStage(),
    ]

# Process the payload through the pipeline with the declared stages
result = await MyPipeline().process(5)

# Returns 30
print(result)
```

In this example, `MyPipeline` declares its stages directly in the class definition, making the pipeline setup more readable and maintainable.

## Declarative Processor

You can also specify the processor in a declarative way by setting the `processor_class` attribute in your pipeline class.

```python
class MyPipeline(Pipeline[T_in, T_out]):
    processor_class = MyCustomProcessor
```

This allows you to customize the processing behavior of your pipeline while keeping the definition clean and declarative.

## Processing Streams

The pipeline can also process streams in real-time, allowing you to handle asynchronous iterators and process data as it becomes available.

```python
from typing import AsyncIterator
import asyncio

async def stage1(stream: AsyncIterator[int]) -> AsyncIterator[int]:
    async for item in stream:
        yield item * 2
        await asyncio.sleep(1)  # Simulate processing delay

async def stage2(stream: AsyncIterator[int]) -> AsyncIterator[str]:
    async for item in stream:
        yield f"Number: {item}"

pipeline = (
    Pipeline[AsyncIterator[int], AsyncIterator[str]]()
    .pipe(stage1)
    .pipe(stage2)
)

async def input_stream() -> AsyncIterator[int]:
    for i in range(5):
        yield i

async def main():
    stream = await pipeline.process(input_stream())

    async for result in stream:
        print(result)

# Run the async main function
asyncio.run(main())
```

This allows you to process data in a streaming fashion, where each stage can yield results that are immediately consumed by the next stage.

## Pipeline Builders

Because pipelines themselves are immutable, pipeline builders are introduced to facilitate distributed composition of a pipeline.

The `PipelineBuilder[InputType, OutputType]` collects stages and allows you to create a pipeline at any given time.

```python
pipeline_builder = (
    PipelineBuilder()
    .add(LogicalStage())
    .add(AnotherStage())
    .add(LastStage())
)

# Build the pipeline
pipeline = pipeline_builder.build()
```

## Exception Handling

This package is completely transparent when dealing with exceptions. In no case will this package catch an exception or silence an error. Exceptions should be dealt with on a per-case basis, either inside a _stage_ or at the time the pipeline processes a payload.

```python
pipeline = Pipeline().pipe(lambda payload: payload / 0)

try:
    await pipeline.process(10)
except ZeroDivisionError as e:
    # Handle the exception.
    pass
```
