from typing import Protocol

from ..with_base.type_payload import TPayload
from ..with_base.stage_interface import (
    StageInterface as WithStageBaseInterface,
)
from ..with_stage_as_callable.stage_interface_mixin import (
    StageInterfaceMixin as WithStageAsCallableInterface,
)


class StageFacade(
    WithStageAsCallableInterface[TPayload],
    WithStageBaseInterface,
    Protocol[TPayload],
):
    pass
