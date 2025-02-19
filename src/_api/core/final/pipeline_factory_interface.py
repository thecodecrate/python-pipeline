from typing import Protocol

from ..partials.step05_pipeline_factory import PipelineFactory_Base_Interface
from ..partials.step06_pipeline_processor import (
    PipelineFactory_WithPipelineProcessor_Interface,
)
from ..partials.step07_pipeline_default_processor import (
    PipelineFactory_WithPipelineDefaultProcessor_Interface,
)
from .types import T_in, T_out


class PipelineFactoryInterface(
    PipelineFactory_WithPipelineDefaultProcessor_Interface[T_in, T_out],
    PipelineFactory_WithPipelineProcessor_Interface[T_in, T_out],
    PipelineFactory_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
