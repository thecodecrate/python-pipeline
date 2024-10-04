from typing import Protocol

from .stage_interface import StageInterface as ImplementsStageInterface


class Stage(
    ImplementsStageInterface,
    Protocol,
):
    pass
