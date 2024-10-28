from abc import abstractmethod
from typing import Any, Optional

from .act_as_factory_interface import ActAsFactoryInterface, TModel


class ActAsFactory(ActAsFactoryInterface[TModel]):
    # set the class here or in `_get_model_class`
    _model_class: Optional[type[TModel]] = None

    @abstractmethod
    def _definition(self) -> dict[str, Any]:
        pass

    def _get_model_class(self) -> type[TModel]:
        if self._model_class is None:
            raise ValueError("Factory _model_class not set")

        return self._model_class

    def make(self) -> TModel:
        instance_class = self._get_model_class()

        return instance_class(**self._definition())
