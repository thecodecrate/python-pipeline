from abc import ABC

from ..step01_base import T_in, T_out
from .pipeline_interface_mixin import PipelineInterfaceMixin as ImplementsInterface
from .processors.chained_processor import ChainedProcessor


class PipelineMixin(
    ImplementsInterface[T_in, T_out],
    ABC,
):
    processor_class = ChainedProcessor
