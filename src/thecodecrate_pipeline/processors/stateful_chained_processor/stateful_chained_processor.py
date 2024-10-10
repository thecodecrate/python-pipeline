from .stateful_chained_command import StatefulChainedCommand
from ...classes.processor import Processor
from ...partials.with_base.types import T_in, T_out


class StatefulChainedProcessor(Processor[T_in, T_out]):
    command_class = StatefulChainedCommand
