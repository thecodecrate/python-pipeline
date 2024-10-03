# TheCodeCrate's Pipeline

This package provides a pipeline pattern implementation.

The implementation is based on the excellent [PHP League Pipeline](https://github.com/thephpleague/pipeline) package.

## Installation

```bash
pip install thecodecrate-pipeline
```

## Pipeline Pattern

The pipeline pattern allows you to easily compose sequential stages by
chaining stages.

In this particular implementation the interface consists of two parts:

- StageInterface
- PipelineInterface

A pipeline consists of zero, one, or multiple stages. A pipeline can process
a payload. During the processing the payload will be passed to the first stage.
From that moment on the resulting value is passed on from stage to stage.

In the simplest form, the execution chain can be represented as a foreach:

```python
result = payload

for stage in stages:
    result = stage(result)

return result
```

Effectively this is the same as:

```python
result = stage3(stage2(stage1(payload)))
```

## Immutability

Pipelines are implemented as immutable stage chains. When you pipe a new
stage, a new pipeline will be created with the added stage. This makes
pipelines easy to reuse, and minimizes side-effects.

## Usage

Operations in a pipeline, stages, can be anything that satisfies the `Callable`
type-hint. So closures and anything that's invokable is good.

```python
pipeline = Pipeline().pipe(lambda payload: payload * 10)

# Returns 100
await pipeline.process(10)
```

## Type hinting

Use `Pipeline[PayloadType]` to type hint the payload type.

```python
pipeline = (
    (Pipeline[int]())
    .pipe(lambda payload: payload * 10)
)

# Returns 100
await pipeline.process(10)
```

## Class based stages

Class based stages are also possible. The `StageInterface[PayloadType]`
can be implemented which ensures you have the correct method signature
for the `__call__` method.

```python
class TimesTwoStage(StageInterface[int]):
    async def __call__(self, payload: int) -> int:
        return payload * 2

class AddOneStage(StageInterface[int]):
    async def __call__(self, payload: int) -> int:
        return payload + 1

pipeline = (
    (Pipeline[int]())
    .pipe(TimesTwoStage())
    .pipe(AddOneStage())
)

# Returns 21
await pipeline.process(10)
```

## Re-usable Pipelines

Because the PipelineInterface is an extension of the StageInterface
pipelines can be re-used as stages. This creates a highly composable model
to create complex execution patterns while keeping the cognitive load low.

For example, if we'd want to compose a pipeline to process API calls, we'd create
something along these lines:

```python
process_api_request = (
    (Pipeline())
    .pipe(ExecuteHttpRequest())
    .pipe(ParseJsonResponse())
)

pipeline = (
    (Pipeline())
    .pipe(ConvertToPsr7Request())
    .pipe(process_api_request)
    .pipe(ConvertToResponseDto())
)

await pipeline.process(DeleteBlogPost(post_id))
```

## Pipeline Builders

Because pipelines themselves are immutable, pipeline builders are introduced to
facilitate distributed composition of a pipeline.

The `PipelineBuilder[PayloadType]` builder collect stages and
allow you to create a pipeline at any given time.

```python
pipeline_builder = (
    (PipelineBuilder())
    .add(LogicalStage())
    .add(AnotherStage())
    .add(LastStage())
)

# Build the pipeline
pipeline = pipeline_builder.build()
```

## Declarative Pipeline Stages

You can define pipeline stages declaratively by specifying them as class-level attributes. This makes it easier to set up and reuse pipelines with predefined stages.

Example:

```python
class MyPipeline(Pipeline[int]):
    processor_class = ChainedProcessor
    stages = [
        TimesTwoStage(),
        TimesThreeStage(),
    ]

# Process the payload through the pipeline with the declared stages
result = await MyPipeline().process(5)

# Returns 30
```

In this example, `MyPipeline` declares its stages (`TimesTwoStage` and `TimesThreeStage`) directly in the class definition, making the pipeline easier to set up and more readable.

This declarative approach allows you to easily reuse pipelines across your project without needing to manually compose them every time.

## Exception handling

This package is completely transparent when dealing with exceptions. In no case
will this package catch an exception or silence an error. Exceptions should be
dealt with on a per-case basis. Either inside a __stage__ or at the time the
pipeline processes a payload.

```python
pipeline = Pipeline().pipe(lambda payload: payload / 0)

try:
    await pipeline.process(10)
except ValueError as e:
    # Handle the exception.
    pass
```
