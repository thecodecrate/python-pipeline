from abc import abstractmethod
from typing import Any, Protocol, TypeVar

TModel = TypeVar("TModel", infer_variance=True)


class ActAsFactoryInterface(Protocol[TModel]):
    @abstractmethod
    def _definition(self) -> dict[str, Any]: ...

    def _get_model_class(self) -> type[TModel]: ...

    def make(self) -> Any: ...
