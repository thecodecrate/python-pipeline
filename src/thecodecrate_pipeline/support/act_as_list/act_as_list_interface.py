from typing import Protocol, Self

from .types import TItem, TCollection


class ActAsListInterface(
    Protocol[TItem, TCollection],
):
    def _get_items(self) -> TCollection: ...

    def _set_items(self, items: TCollection) -> Self: ...

    def _add_item(self, item: TItem) -> Self: ...
