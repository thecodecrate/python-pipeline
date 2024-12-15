from abc import abstractmethod
from typing import Protocol, Self

from .types import TItem, TCollection
from .act_as_list_interface import ActAsListInterface


class ActAsList(
    ActAsListInterface[TItem, TCollection],
    Protocol[TItem, TCollection],
):
    @abstractmethod
    def _get_items(self) -> TCollection:
        pass

    @abstractmethod
    def _set_items(self, items: TCollection) -> Self:
        pass

    @abstractmethod
    def _add_item(self, item: TItem) -> Self:
        pass
