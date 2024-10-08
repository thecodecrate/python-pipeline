from typing import Any, TypeVar

T_in = TypeVar("T_in", default=Any, infer_variance=True)

T_out = TypeVar("T_out", default=T_in, infer_variance=True)
