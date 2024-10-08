from typing import Protocol

from ..partials.with_base.payload_type import TPayload
from ..partials.with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)


class ProcessorInterface(
    WithProcessorBaseInterface[TPayload],
    Protocol[TPayload],
):
    pass
