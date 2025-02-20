from abc import ABC
from typing import Optional

# uses: base concrete
from ..bases.processors.chained_processor import ChainedProcessor

# extends: self-bridge concrete
from ..bridges.pipeline import Pipeline

# uses: bridge interface
from ..bridges.processor_interface import ProcessorInterface
from ..bridges.types import T_in, T_out

# implements: self-interface
from .pipeline_interface_mixin import PipelineInterfaceMixin as ImplementsInterface


class PipelineMixin(
    Pipeline[T_in, T_out],
    ImplementsInterface[T_in, T_out],
    ABC,
):
    processor_class: Optional[type[ProcessorInterface]] = ChainedProcessor[T_in, T_out]
