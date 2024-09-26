from abc import ABC
from typing import Generic
from ...traits.with_parts.with_parts import WithParts
from .types import TBuilderOutput, TBuilderPart


class Builderable(
    WithParts[
        "Builderable[TBuilderOutput, TBuilderPart]",
        TBuilderOutput,
        TBuilderPart,
    ],
    Generic[TBuilderOutput, TBuilderPart],
    ABC,
):
    def __init__(self) -> None:
        self.set_parts([])
