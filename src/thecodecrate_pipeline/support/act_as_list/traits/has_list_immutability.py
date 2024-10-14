import copy
from typing import Protocol, Self

from ..act_as_list_interface import ActAsListInterface
from ..item import TItem


class HasListImmutability(
    ActAsListInterface[TItem],
    Protocol[TItem],
):
    def _add_item(self, item: TItem) -> Self:
        cloned = copy.deepcopy(self)

        cloned._get_items().append(item)

        return cloned
