from typing import Protocol

from .pipeline_interface import (
    PipelineInterface as ImplementsPipelineInterface,
)


class Pipeline(
    ImplementsPipelineInterface,
    Protocol,
):
    pass
