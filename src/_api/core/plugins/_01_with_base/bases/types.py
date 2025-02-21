from typing import Any, TypeVar

T_in = TypeVar("T_in", default=Any, infer_variance=True)
"""Input data type for pipeline flow (payload's value type)"""

T_out = TypeVar("T_out", default=T_in, infer_variance=True)
"""Output data type for pipeline flow (result's value type)"""
