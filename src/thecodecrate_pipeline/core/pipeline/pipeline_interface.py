from abc import ABC
from typing import Generic

from ...support.libraries.builderable import Builderable, WithImmutability
from ...traits.with_stages.with_stages import WithStages
from ...traits.with_processor.with_processor import WithProcessor
from ...traits.with_stages.stage_interface import StageOrCallable
from .payload import TPayload


class PipelineInterface(
    WithProcessor["PipelineInterface[TPayload]", TPayload],
    WithStages["PipelineInterface[TPayload]", TPayload],
    WithImmutability[
        "PipelineInterface[TPayload, StageOrCallable[TPayload]]",
        TPayload,
        StageOrCallable[TPayload],
    ],
    Builderable[TPayload, StageOrCallable[TPayload]],
    Generic[TPayload],
    ABC,
):
    pass
