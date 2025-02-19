from typing import Protocol

from ..step01_base import Pipeline_Base_Interface, T_in, T_out
from ..step02_pipeline_as_list import Pipeline_WithPipelineAsList_Interface
from ..step06_pipeline_processor import Pipeline_WithPipelineProcessor_Interface


class PipelineInterfaceMixin(
    Pipeline_WithPipelineProcessor_Interface,
    Pipeline_WithPipelineAsList_Interface,
    Pipeline_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
