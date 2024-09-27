from thecodecrate_pipeline import StageInterface


class TimesTwoStage(StageInterface[int]):
    async def __call__(self, payload: int) -> int:
        return payload * 2


class AddOneStage(StageInterface[int]):
    async def __call__(self, payload: int) -> int:
        return payload + 1


class TimesThreeStage(StageInterface[int]):
    async def __call__(self, payload: int) -> int:
        return payload * 3
