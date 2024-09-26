import pytest

from thecodecrate_pipeline.support.libraries.builderable import (
    Builderable,
    WithImmutability,
)


class BuilderMutable(Builderable[str, int]):
    parts: list[int] = []

    def build_parts(self, payload: int) -> str:
        result = payload + sum(self.get_parts())

        return f"result is {result}"


class BuilderImmutable(
    WithImmutability["BuilderImmutable[str, int]", str, int],
    Builderable[str, int],
):
    parts: list[int] = []

    def build_parts(self, payload: int) -> str:
        result = payload + sum(self.get_parts())

        return f"result is {result}"


@pytest.mark.asyncio
async def test_builderable_base():
    builder = (BuilderMutable()).add(1).add(2).add(3)

    assert builder.get_parts() == [1, 2, 3]
    assert builder.build_parts(0) == "result is 6"
    assert builder.add(4).get_parts() == [1, 2, 3, 4]
    assert builder.build_parts(5) == "result is 15"


@pytest.mark.asyncio
async def test_new_instances_dont_share_parts():
    builder1 = (BuilderMutable()).add(1).add(2).add(3)
    assert builder1.get_parts() == [1, 2, 3]
    assert builder1.build_parts(0) == "result is 6"

    builder2 = (BuilderMutable()).add(4).add(5).add(6)
    assert builder2.get_parts() == [4, 5, 6]
    assert builder2.build_parts(0) == "result is 15"


@pytest.mark.asyncio
async def test_inheritance():
    class SubBuilder(BuilderMutable):
        def build_parts(self, payload: int) -> str:
            result = payload + sum(self.get_parts())

            return f"sub result is {result}"

    builder = (SubBuilder()).add(1).add(2).add(3)

    assert builder.get_parts() == [1, 2, 3]
    assert builder.build_parts(0) == "sub result is 6"
    assert builder.add(4).get_parts() == [1, 2, 3, 4]
    assert builder.build_parts(5) == "sub result is 15"


@pytest.mark.asyncio
async def test_immutability():
    builder = (BuilderImmutable()).add(1).add(2).add(3)
    builder2 = builder.add(4)

    assert builder.get_parts() == [1, 2, 3]
    assert builder2.get_parts() == [1, 2, 3, 4]

    assert builder.build_parts(5) == "result is 11"
    assert builder2.build_parts(5) == "result is 15"


@pytest.mark.asyncio
async def test_mutability():
    builder = (BuilderMutable()).add(1).add(2).add(3)
    builder2 = builder.add(4)

    assert builder.get_parts() == [1, 2, 3, 4]
    assert builder2.get_parts() == [1, 2, 3, 4]
