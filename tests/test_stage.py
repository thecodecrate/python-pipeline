# pyright: reportUnusedFunction=false
import inspect
from typing import Any, Callable, Protocol, runtime_checkable

import pytest
from pytest_describe import behaves_like  # type: ignore

from thecodecrate_pipeline import Stage, StageCallable


def _is_stage_callable(stage: StageCallable) -> bool:
    """
    Validates if a given stage implements the StageCallable interface.

    Args:
        stage (StageCallable): The stage to validate.

    Returns:
        bool: True if the stage is a valid callable conforming to StageCallable
        interface.
    """

    @runtime_checkable
    class StageCallableProtocol(StageCallable, Protocol):
        pass

    return isinstance(stage, StageCallableProtocol)


def a_stage_callable() -> None:
    """
    Defines shared behavior tests for stage callables.

    This test suite verifies:
    1. Stage implements the StageCallable interface
    2. Stage produces expected outputs for given inputs

    Required Fixtures:
        - stage: The stage implementation to test
        - expected_results: List of (input, expected_output) tuples for testing

    Note:
        This is a shared behavior suite used with @behaves_like decorator.
    """

    def it_is_stage_callable(stage: StageCallable):
        assert _is_stage_callable(stage)

    @pytest.mark.asyncio
    async def it_returns_correctly(
        stage: StageCallable, expected_results: list[tuple[Any, Any]]
    ):
        for input_value, expected in expected_results:
            result = stage(input_value)

            if inspect.isawaitable(result):
                result = await result

            assert result == expected


def describe_stage():
    @behaves_like(a_stage_callable)
    def describe_stage_can_be_class_based():
        @pytest.fixture
        def stage():
            class AsyncStage(Stage[int, int]):
                async def __call__(self, payload: int) -> int:
                    return payload * 5

            return AsyncStage()

        @pytest.fixture
        def expected_results() -> list[tuple[int, int]]:
            return [(-1, -5), (5, 25)]

    @behaves_like(a_stage_callable)
    def describe_stage_can_be_function_based():
        @pytest.fixture
        def stage():
            async def async_stage(payload: int) -> int:
                return payload * 5

            return async_stage

        @pytest.fixture
        def expected_results() -> list[tuple[int, int]]:
            return [(-1, -5), (5, 25)]

        @behaves_like(a_stage_callable)
        def describe_function_can_be_sync():
            @pytest.fixture
            def stage():
                def sync_stage(payload: int) -> int:
                    return payload * 5

                return sync_stage

            @pytest.fixture
            def expected_results() -> list[tuple[int, int]]:
                return [(-1, -5), (5, 25)]

    @behaves_like(a_stage_callable)
    def describe_stage_can_be_lambda_based():
        @pytest.fixture
        def stage():
            lambda_stage: Callable[[int], int] = lambda payload: payload * 5
            return lambda_stage

        @pytest.fixture
        def expected_results() -> list[tuple[int, int]]:
            return [(-1, -5), (5, 25)]

    def describe_payload_argument():
        @behaves_like(a_stage_callable)
        def describe_payload_can_have_any_name():
            @pytest.fixture
            def stage():
                class AsyncStage(Stage[int, int]):
                    async def __call__(self, x: int) -> int:
                        return x * 5

                return AsyncStage()

            @pytest.fixture
            def expected_results() -> list[tuple[int, int]]:
                return [(-1, -5), (5, 25)]

        @behaves_like(a_stage_callable)
        def describe_payload_accepts_different_types():
            @pytest.fixture
            def stage():
                def sync_stage(payload: str) -> int:
                    return int(payload) * 5

                return sync_stage

            @pytest.fixture
            def expected_results() -> list[tuple[str, int]]:
                return [("-1", -5), ("5", 25)]
