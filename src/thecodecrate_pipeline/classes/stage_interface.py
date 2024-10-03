from typing import Protocol

from ..partials.with_base.type_payload import TPayload
from ..partials.with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..partials.with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)


class StageInterface(
    WithStageAsCallableInterface[TPayload],
    WithStageBaseInterface,
    Protocol[TPayload],
):
    pass
