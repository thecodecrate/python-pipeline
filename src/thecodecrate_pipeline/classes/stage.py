from .stage_interface import StageInterface as ImplementsStageInterface
from ..partials.with_base.type_payload import TPayload
from ..partials.with_base.stage import (
    Stage as WithStageBaseConcern,
)
from ..partials.with_stage_as_callable.stage_mixin import (
    StageMixin as WithStageAsCallableConcern,
)


class Stage(
    WithStageAsCallableConcern[TPayload],
    WithStageBaseConcern,
    ImplementsStageInterface[TPayload],
):
    pass
