## Features

This plugin provides the following features:

### `Pipeline` class

The pipeline class accepts a list of callbacks to be executed in order.

```python
pipeline = (
    (Pipeline())
    .pipe(lambda payload: payload + 1)
    .pipe(lambda payload: payload * 2)
    .pipe(lambda payload: payload + 1)
)
```

### Processing Payloads

You can process payloads through the pipeline using the `process` method.

```python
result = await pipeline.process(5)
```

### Type hinting

You can specify the input and output types for pipelines and stages using type variables `T_in` and `T_out`. This allows you to handle varying types between stages, enhancing type safety and code clarity. `T_in` is the type of the payload value, and `T_out` is the type of the return value.

```python
pipeline = Pipeline[int, str](callbacks)

# Returns "Number: 10"
await pipeline.process(10)
```

### Immutability

Pipelines are implemented as immutable stage chains. You cannot modify the pipeline after it has been created.
