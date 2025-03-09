# region IMPORTS
from typing import Union as __Union, Literal as __Literal, Collection as __Collection, Iterable as __Iterable
# endregion


# region TYPES
SupportsIn = __Union[str, __Iterable, __Collection]
real_number = __Union[int, float]

overflow_options = __Literal[
    "trunc_right", "tr",
    "trunc_left",  "tl",
    "wrap_max",   "wm",
    "wrap_equal", "we",
    "wrap_words", "ww"
]
# endregion


# region EXPORTS
__all__ = [
    name
    for name in globals().keys()
    if not name.startswith("__")
]
# endregion
