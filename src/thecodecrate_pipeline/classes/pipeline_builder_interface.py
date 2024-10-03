from typing import Protocol

from ..partials.with_base.type_payload import TPayload
from ..partials.with_base.pipeline_interface import (
    PipelineInterface as WithPipelineBaseInterface,
)
from ..partials.with_pipeline_as_list.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithPipelineAsListInterface,
)
from ..partials.with_builder_methods.pipeline_interface_mixin import (
    PipelineInterfaceMixin as WithBuilderMethodsInterface,
)


class PipelineBuilderInterface(
    WithBuilderMethodsInterface[TPayload],
    WithPipelineAsListInterface[TPayload],
    WithPipelineBaseInterface,
    Protocol[TPayload],
):
    pass
