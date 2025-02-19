from typing import Protocol

from ..step01_base import Pipeline_Base_Interface, T_in, T_out
from ..step02_pipeline_as_list import Pipeline_WithPipelineAsList_Interface
from ..step06_pipeline_processor import Pipeline_WithPipelineProcessor_Interface
from ..step07_pipeline_default_processor import (
    Pipeline_WithPipelineDefaultProcessor_Interface,
)
from .stage_stub_interface import StageStubInterface


class PipelineInterfaceMixin(
    StageStubInterface[T_in, T_out],
    Pipeline_WithPipelineDefaultProcessor_Interface[T_in, T_out],
    Pipeline_WithPipelineProcessor_Interface[T_in, T_out],
    Pipeline_WithPipelineAsList_Interface,
    Pipeline_Base_Interface,
    Protocol[T_in, T_out],
):
    pass
