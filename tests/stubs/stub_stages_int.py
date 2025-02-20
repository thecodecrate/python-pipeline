from thecodecrate_pipeline import Stage


class TimesTwoStage(Stage[int]):
    async def __call__(self, payload: int) -> int:
        return payload * 2


class AddOneStage(Stage[int]):
    async def __call__(self, payload: int) -> int:
        return payload + 1


class InvalidStage(Stage[int]):
    async def __call__(self, payload: str) -> int:
        return len(payload)


class TimesThreeStage(Stage[int]):
    async def __call__(self, payload: int) -> int:
        return payload * 3
