# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `thecodecrate-pipeline`, a Python package that provides a pipeline pattern implementation for data processing. Pipelines allow chaining multiple stages together, where each stage transforms a payload before passing it to the next stage.

**Key Concepts:**

- **Pipeline**: Orchestrates the execution of multiple stages using a processor
- **Stage**: A callable unit that transforms a payload (input → output)
- **Processor**: Defines how stages are executed (e.g., chained, interruptible)
- **PipelineFactory**: Creates pipeline instances with predefined stages and processors

## Architecture

### Code Organization

The codebase follows a concern-based architecture with clear separation between contracts, concerns, and implementations:

```
src/
├── thecodecrate_pipeline/     # Public API
│   └── __init__.py            # Re-exports main classes
└── _lib/                      # Internal implementation
    ├── contracts/             # Protocol definitions (interfaces)
    ├── concerns/              # Mixins for shared behavior
    ├── processors/            # Processor implementations
    ├── support/               # Utility patterns (Clonable, ActAsFactory)
    └── types/                 # Type definitions
```

### Key Design Patterns

**Concerns Pattern**: The Pipeline class inherits from multiple concern classes (BasePipeline, ProcessablePipeline, StageablePipeline), each providing specific functionality. This follows a composition-over-inheritance approach where each concern is responsible for a single aspect:

- `BasePipeline`: Core cloning and factory behavior
- `ProcessablePipeline`: Handles processor management and execution (src/_lib/concerns/processable_pipeline.py)
- `StageablePipeline`: Manages stage collection and instantiation (src/_lib/concerns/stageable_pipeline.py)

**Contracts (Protocols)**: All contracts are defined using Python's `Protocol` type for structural subtyping. Implementations explicitly declare they implement these protocols via inheritance.

**Clonable Pattern**: Most classes inherit from `Clonable` (src/_lib/support/clonable/clonable.py), which provides immutable-style operations using deep copying. Methods like `pipe()`, `with_stages()`, and `with_processor()` return cloned instances rather than mutating the original.

**ActAsFactory Pattern**: The `PipelineFactory` uses this pattern (src/_lib/support/act_as_factory/) to create pipeline instances with predefined configuration.

### Type System

The codebase is fully typed using generic types `T_in` and `T_out` for input/output payloads. All classes are generic over these types to ensure type safety through the pipeline chain.

## Development Commands

### Environment Setup

```bash
# Install uv package manager if not available
uv python install 3.13
uv sync --all-extras --dev
```

### Testing

```bash
# Run all tests with coverage
uv run pytest tests --cov

# Run a specific test file
uv run pytest tests/test_pipeline.py

# Run a specific test
uv run pytest tests/test_pipeline.py::test_lambda_stages -v
```

### Linting & Formatting

```bash
# Check linting
uvx ruff check .

# Fix linting issues automatically
uvx ruff check --fix .

# Format code
uvx ruff format .
```

### Version Bumping

```bash
# Bump version (patch/minor/major)
uv run bumpver update --patch
uv run bumpver update --minor
uv run bumpver update --major
```

Version is managed by bumpver and automatically updates:

- `pyproject.toml`
- `src/thecodecrate_pipeline/__init__.py`

### Documentation

```bash
# Build documentation locally
mkdocs serve

# Build static site
mkdocs build
```

## Important Implementation Details

### Async Processing

All pipeline processing is async. The `Pipeline.process()` method and all stage `__call__` methods are async. The base `Processor._call()` method (src/_lib/processor.py:37-52) handles both sync and async callables automatically using `inspect.isawaitable()`.

### Stage Instantiation

Stages can be provided as either classes or instances. The `StageablePipeline` concern automatically instantiates stage classes when needed (src/_lib/concerns/stageable_pipeline.py:67-72).

### Processor Types

- `ChainedProcessor`: Default processor that executes stages sequentially (src/_lib/processors/chained_processor/)
- `InterruptibleProcessor`: Allows stages to interrupt the pipeline flow (src/_lib/processors/interruptible_processor/)

### Callable Invocation

The `Pipeline` class is callable and delegates to `process()` (src/_lib/concerns/processable_pipeline.py:52-62). The first parameter is positional-only to match the callable signature.

## Testing Guidelines

- All async tests must be marked with `@pytest.mark.asyncio`
- Test stubs are located in `tests/stubs/`
- Tests cover: lambda stages, class-based stages, pipeline-as-stage, custom processors, and factory patterns
- The pytest configuration sets `asyncio_default_fixture_loop_scope = function`
