from abc import abstractmethod
from typing import Protocol, Self
from .item import TItem
from .act_as_list_interface import ActAsListInterface


class ActAsList(
    ActAsListInterface[TItem],
    Protocol[TItem],
):
    @abstractmethod
    def _get_items(self) -> list[TItem]:
        pass

    @abstractmethod
    def _set_items(self, items: list[TItem]) -> Self:
        pass

    def _add_item(self, item: TItem) -> Self:
        self._get_items().append(item)

        return self
