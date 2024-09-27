from typing import Generic

from .payload import TPayload
from .pipeline_interface import PipelineInterface
from ...modules.processors.chained_processor import ChainedProcessor


class Pipeline(
    PipelineInterface[TPayload],
    Generic[TPayload],
):
    processor_class = ChainedProcessor
