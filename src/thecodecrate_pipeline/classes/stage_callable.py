from typing import Protocol
from ..partials.with_base.payload_type import TPayload
from ..partials.with_base.stage_callable import (
    StageCallable as WithStageCallableBase,
)


class StageCallable(
    WithStageCallableBase[TPayload],
    Protocol[TPayload],
):
    pass
