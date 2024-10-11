from abc import ABC
from typing import Self

from ..with_base.types import T_in, T_out
from ..with_base.stage_callable import StageCallableType
from .pipeline_interface_mixin import (
    PipelineInterfaceMixin as ImplementsPipelineInterface,
)


class PipelineMixin(
    ImplementsPipelineInterface[T_in, T_out],
    ABC,
):
    def pipe(self, stage: StageCallableType) -> Self:
        return self.add_item(stage)
