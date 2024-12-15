from typing import Any, Sequence, TypeVar

TItem = TypeVar("TItem", infer_variance=True)

TCollection = TypeVar("TCollection", infer_variance=True, bound=Sequence[Any])
