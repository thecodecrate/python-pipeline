from typing import Protocol

from ..step01_base import Stage_Base_Interface, T_in, T_out
from ..step03_stage_as_callable import Stage_WithStageAsCallable_Interface


class StageStubInterface(
    Stage_WithStageAsCallable_Interface[T_in, T_out],
    Stage_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
