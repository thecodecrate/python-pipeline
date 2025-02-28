from abc import abstractmethod
from typing import Any, Optional

from .act_as_factory_interface import ActAsFactoryInterface, T_target


class ActAsFactory(ActAsFactoryInterface[T_target]):
    # set the class here or in `_get_target_class`
    _target_class: Optional[type[T_target]] = None

    @abstractmethod
    def _definition(self) -> dict[str, Any]:
        pass

    def _get_target_class(self) -> type[T_target]:
        if self._target_class is None:
            raise ValueError("Factory _target_class not set")

        return self._target_class

    def make(self) -> T_target:
        instance_class = self._get_target_class()

        return instance_class(**self._definition())
