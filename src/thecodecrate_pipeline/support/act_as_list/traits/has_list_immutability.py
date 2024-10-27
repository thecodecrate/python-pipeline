import copy
from typing import Protocol, Self

from .has_list_immutability_interface import HasListImmutabilityInterface
from ..item import TItem


class HasListImmutability(
    HasListImmutabilityInterface[TItem],
    Protocol[TItem],
):
    def _add_item(self, item: TItem) -> Self:
        cloned = copy.deepcopy(self)

        cloned._get_items().append(item)

        return cloned
