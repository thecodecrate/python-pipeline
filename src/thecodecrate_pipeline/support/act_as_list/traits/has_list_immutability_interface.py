from typing import Protocol, Self

from ..act_as_list_interface import ActAsListInterface
from ..item import TItem


class HasListImmutabilityInterface(
    ActAsListInterface[TItem],
    Protocol[TItem],
):
    def _add_item(self, item: TItem) -> Self: ...
