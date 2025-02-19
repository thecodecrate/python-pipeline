from typing import Generic

from ..partials.step07_pipeline_default_processor import ChainedProcessor_Base
from .types import T_in, T_out


class ChainedProcessor(
    ChainedProcessor_Base[T_in, T_out],
    Generic[T_in, T_out],
):
    pass
