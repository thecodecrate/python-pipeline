from typing import Any, Protocol, TypeVar

from ..with_base.types import T_in, T_out
from ..with_processor_commands.command_interface import (
    CommandInterface as WithCommandBaseInterface,
)


class CommandFacade(
    WithCommandBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass


TCommand = TypeVar(
    "TCommand", bound=CommandFacade[Any, Any], infer_variance=True
)
