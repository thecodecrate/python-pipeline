from typing import Protocol

from ..partials.with_base.types import T_in, T_out
from ..partials.with_processor_commands.command_interface import (
    CommandInterface as WithCommandBaseInterface,
)


class CommandInterface(
    WithCommandBaseInterface[T_in, T_out],
    Protocol[T_in, T_out],
):
    pass
