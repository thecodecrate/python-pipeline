from thecodecrate_pipeline import StageInterface


class StubStage(StageInterface[str]):
    STUBBED_RESPONSE = "stubbed response"

    def __call__(self, payload: str) -> str:
        return self.STUBBED_RESPONSE
