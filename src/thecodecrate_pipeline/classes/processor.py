from .processor_interface import (
    ProcessorInterface as ImplementsProcessorInterface,
)
from ..partials.with_base.type_payload import TPayload
from ..partials.with_pipeline_processor.processor import (
    Processor as WithProcessorBaseConcern,
)


class Processor(
    WithProcessorBaseConcern[TPayload],
    ImplementsProcessorInterface[TPayload],
):
    pass
