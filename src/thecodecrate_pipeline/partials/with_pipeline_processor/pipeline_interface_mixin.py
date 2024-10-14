from typing import Any, Protocol

from .processor_interface import ProcessorInterface
from ..with_base.types import T_in, T_out
from ..with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)


class PipelineInterfaceMixin(
    WithPipelineAsListInterface,
    WithPipelineBaseInterface,
    Protocol[T_in, T_out],
):
    def _make_processor(self) -> ProcessorInterface: ...

    async def process(
        self, payload: T_in, *args: Any, **kwds: Any
    ) -> T_out: ...
