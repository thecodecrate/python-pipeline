import copy
from typing import Protocol, Self

from ..renamable_list_interface import RenamableListInterface
from ..item_type import TItem


class HasImmutability(
    RenamableListInterface[TItem],
    Protocol[TItem],
):
    def add_item(self, item: TItem) -> Self:
        cloned = copy.deepcopy(self)

        cloned.get_items().append(item)

        return cloned
