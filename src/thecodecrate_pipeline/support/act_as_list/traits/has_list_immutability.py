import copy
from typing import Protocol, Self

from ..act_as_list_interface import ActAsListInterface
from ..item import TItem


class HasListImmutability(
    ActAsListInterface[TItem],
    Protocol[TItem],
):
    def add_item(self, item: TItem) -> Self:
        cloned = copy.deepcopy(self)

        cloned.get_items().append(item)

        return cloned
