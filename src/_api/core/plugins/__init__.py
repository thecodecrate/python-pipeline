from ._01_with_base import __all__ as _01_with_base
from ._02_with_pipeline_as_list import __all__ as _02_with_pipeline_as_list
from ._03_with_stage_as_callable import __all__ as _03_with_stage_as_callable
from ._04_with_pipeline_declared_stages import (
    __all__ as _04_with_pipeline_declared_stages,
)
from ._05_with_pipeline_factory import __all__ as _05_with_pipeline_factory
from ._06_with_pipeline_processor import __all__ as _06_with_pipeline_processor
from ._08_with_pipeline_as_stage import __all__ as _08_with_pipeline_as_stage
from ._99_with_pipeline_default_processor import (
    __all__ as _99_with_pipeline_default_processor,
)

# pyright: reportUnsupportedDunderAll=false
__all__ = (
    *_01_with_base,
    *_02_with_pipeline_as_list,
    *_03_with_stage_as_callable,
    *_04_with_pipeline_declared_stages,
    *_05_with_pipeline_factory,
    *_06_with_pipeline_processor,
    *_08_with_pipeline_as_stage,
    *_99_with_pipeline_default_processor,
)
