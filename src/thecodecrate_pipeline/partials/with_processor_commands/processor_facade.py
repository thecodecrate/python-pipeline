from typing import Any, Protocol, TypeVar

from ..with_base.types import T_in, T_out
from ..with_pipeline_processor.processor_interface import (
    ProcessorInterface as WithProcessorBaseInterface,
)


class ProcessorFacade(
    WithProcessorBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


TProcessor = TypeVar("TProcessor", bound=ProcessorFacade[Any, Any])
