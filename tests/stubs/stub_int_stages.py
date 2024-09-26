from thecodecrate_pipeline import StageInterface


class TimesTwoStage(StageInterface[int]):
    def __call__(self, payload: int) -> int:
        return payload * 2


class AddOneStage(StageInterface[int]):
    def __call__(self, payload: int) -> int:
        return payload + 1


class TimesThreeStage(StageInterface[int]):
    def __call__(self, payload: int) -> int:
        return payload * 3
