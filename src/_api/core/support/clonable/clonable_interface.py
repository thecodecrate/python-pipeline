from typing import Any, Protocol, Self


class ClonableInterface(Protocol):
    def clone(self, attributes: dict[str, Any]) -> Self: ...
