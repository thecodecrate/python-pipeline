from typing import Any, Protocol, TypeVar

from ..partials.with_base.types import T_in, T_out
from ..partials.with_processor_commands.command_interface import (
    CommandInterface as WithCommandBaseInterface,
)


class CommandInterface(
    WithCommandBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


TCommand = TypeVar(
    "TCommand", bound=CommandInterface[Any, Any], infer_variance=True
)
