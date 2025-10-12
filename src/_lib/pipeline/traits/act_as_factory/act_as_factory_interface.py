from abc import abstractmethod
from typing import Any, Protocol, TypeVar

T_target = TypeVar("T_target", infer_variance=True)


class ActAsFactoryInterface(Protocol[T_target]):
    @abstractmethod
    def _definition(self) -> dict[str, Any]: ...

    def _get_target_class(self) -> type[T_target]: ...

    def make(self) -> Any: ...
