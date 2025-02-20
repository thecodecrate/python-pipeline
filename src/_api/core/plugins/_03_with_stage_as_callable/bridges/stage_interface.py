from typing import Protocol

# extends: outside base
from ..._01_with_base import StageInterface as StageBaseInterface


class StageInterface(
    StageBaseInterface,
    Protocol,
):
    pass
