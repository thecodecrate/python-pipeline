from abc import abstractmethod
from typing import Protocol, Self
from .item_type import TItem
from .renamable_list_interface import RenamableListInterface


class RenamableList(
    RenamableListInterface[TItem],
    Protocol[TItem],
):
    @abstractmethod
    def get_items(self) -> list[TItem]:
        pass

    @abstractmethod
    def set_items(self, items: list[TItem]) -> Self:
        pass

    def add_item(self, item: TItem) -> Self:
        self.get_items().append(item)

        return self
