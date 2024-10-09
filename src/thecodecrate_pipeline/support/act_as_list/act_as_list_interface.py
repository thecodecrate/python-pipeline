from typing import Protocol, Self

from .item import TItem


class ActAsListInterface(
    Protocol[TItem],
):
    def get_items(self) -> list[TItem]: ...

    def set_items(self, items: list[TItem]) -> Self: ...

    def add_item(self, item: TItem) -> Self: ...
