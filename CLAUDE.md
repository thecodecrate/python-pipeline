# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python implementation of the Pipeline pattern, distributed as `thecodecrate-pipeline`. The package allows composing sequential stages into reusable, immutable pipelines for processing data. It's inspired by the PHP League Pipeline package.

## Development Commands

### Environment Setup
```bash
# The project uses uv for dependency management
# Dependencies are managed in pyproject.toml under [dependency-groups]
uv sync
```

### Testing
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run a specific test file
pytest tests/test_pipeline.py

# Run a specific test function
pytest tests/test_pipeline.py::test_function_name
```

### Code Quality
```bash
# Format code with ruff
ruff format .

# Lint with ruff
ruff check .

# Fix auto-fixable linting issues
ruff check --fix .

# Format with black (line length: 79)
black .

# Type checking is configured with strict mode in pyrightconfig.json
# Type check manually: pyright (if installed)
```

### Documentation
```bash
# Build documentation locally
mkdocs serve

# Documentation is built with mkdocs-material and auto-generates API docs
# from docstrings using mkdocstrings-python
```

### Version Management
```bash
# Bump version (uses bumpver)
bumpver update --patch   # 1.26.0 -> 1.26.1
bumpver update --minor   # 1.26.0 -> 1.27.0
bumpver update --major   # 1.26.0 -> 2.0.0

# Note: bumpver automatically commits and tags, but does NOT push
```

## Architecture

### Core Concepts

The codebase implements a pipeline pattern with three main abstractions:

1. **Stage**: A callable unit that transforms input to output (`StageInterface[T_in, T_out]`)
2. **Pipeline**: An immutable chain of stages (`PipelineInterface[T_in, T_out]`)
3. **Processor**: Controls how stages are executed (`ProcessorInterface[T_in, T_out]`)

### Directory Structure

```
src/
├── _lib/                           # Internal implementation
│   ├── pipeline/                   # Core pipeline implementation
│   │   ├── pipeline.py            # Main Pipeline class
│   │   ├── pipeline_factory.py   # Factory for building pipelines
│   │   ├── processor.py           # Base Processor class
│   │   ├── stage.py               # Base Stage class
│   │   ├── processors/            # Built-in processors
│   │   │   ├── chained_processor.py
│   │   │   └── ...
│   │   └── traits/                # Mixins (Clonable, ActAsFactory)
│   └── processors/                # Additional processor implementations
│       ├── chained_processor/     # Processor that chains stages
│       └── interruptible_processor/ # Processor with interruption support
└── thecodecrate_pipeline/         # Public API package
    ├── __init__.py                # Re-exports from _lib
    ├── processors/                # Public processor exports
    └── types/                     # Public type exports
```

### Key Design Patterns

**Immutability**: Pipelines use copy-on-write semantics. The `pipe()` method creates a new pipeline instance with the added stage, preserving the original pipeline.

**Traits System**: The codebase uses a trait-like pattern with mixins:
- `Clonable`: Provides shallow cloning capability
- `ActAsFactory`: Enables objects to act as factories for creating instances

**Interface Segregation**: Each core concept has an interface (`*Interface`) and implementation, enabling custom implementations while maintaining type safety.

**Async-First**: All processing is async (`async def process(...)`). The processor handles both sync and async callables transparently using `inspect.isawaitable()`.

### Type System

The codebase uses generic type variables for type safety:
- `T_in`: Input type to a stage or pipeline
- `T_out`: Output type from a stage or pipeline (defaults to `T_in`)

Stages can transform types:
```python
Pipeline[int, str]  # Takes int, returns str
StageInterface[int, int]  # Takes int, returns int
```

### Processing Flow

1. A Pipeline is created with stages (either via `.pipe()` or declaratively)
2. When `.process(payload)` is called, the pipeline:
   - Instantiates stages if needed (converts classes to instances)
   - Delegates to the processor's `.process()` method
   - The processor iterates through stages, passing output to next stage
3. Processors can customize execution (e.g., ChainedProcessor for error handling)

### Stream Processing

Pipelines support processing `AsyncIterator` streams, allowing real-time data transformation where each stage can yield results consumed immediately by the next stage.

### PipelineFactory

Because pipelines are immutable, `PipelineFactory` provides mutable stage collection during composition. It builds the final immutable pipeline via `.build()`.

## Testing Notes

- Test files use stub classes in `tests/stubs/` for consistent test fixtures
- Tests are async-aware (configured via `pytest.ini` with `pytest-asyncio`)
- Mock stages implement `StageInterface` for type safety

## Python Version

Requires Python 3.13+ (specified in pyproject.toml).

## Package Distribution

Built with `hatchling`. The wheel includes both `thecodecrate_pipeline` (public API) and `_api` packages (internal). The public package re-exports symbols from `_lib`.
