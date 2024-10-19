from abc import ABC

from .command_interface import (
    CommandInterface as ImplementsCommandInterface,
)
from ..partials.with_base.types import T_in, T_out
from ..partials.with_processor_commands.command import (
    Command as WithCommandBaseConcern,
)


class Command(
    WithCommandBaseConcern[T_in, T_out],
    ImplementsCommandInterface[T_in, T_out],
    ABC,
):
    pass
