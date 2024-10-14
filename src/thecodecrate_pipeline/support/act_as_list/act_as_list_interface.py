from typing import Protocol, Self

from .item import TItem


class ActAsListInterface(
    Protocol[TItem],
):
    def _get_items(self) -> list[TItem]: ...

    def _set_items(self, items: list[TItem]) -> Self: ...

    def _add_item(self, item: TItem) -> Self: ...
