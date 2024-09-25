from abc import ABC
from typing import Generic

from .parent_class import TParentClass
from ...core.pipeline.payload import TPayload


class WithStages(
    Generic[TParentClass, TPayload],
    ABC,
):
    pass
