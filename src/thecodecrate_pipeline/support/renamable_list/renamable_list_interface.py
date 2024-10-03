from typing import Protocol, Self

from .item_type import TItem


class RenamableListInterface(
    Protocol[TItem],
):
    def get_items(self) -> list[TItem]: ...

    def set_items(self, items: list[TItem]) -> Self: ...

    def add_item(self, item: TItem) -> Self: ...
