from typing import Protocol

from ..step01_base import Pipeline_Base_Interface, T_in, T_out
from ..step05_pipeline_factory import PipelineFactory_Base_Interface
from ..step06_pipeline_processor import (
    PipelineFactory_WithPipelineProcessor_Interface,
)


class PipelineFactoryInterfaceMixin(
    PipelineFactory_WithPipelineProcessor_Interface[T_in, T_out],
    PipelineFactory_Base_Interface[Pipeline_Base_Interface],
    Protocol[T_in, T_out],
):
    pass
