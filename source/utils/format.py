from math import floor
from typing import Any, Union, List, Optional

from globals_and_types import SupportsIn
from globals_and_types import overflow_options


def wrap_by_words(
        obj: Union[str, Any],
        line_length: int = 120,
        as_list: bool = False,
        allowed_punctuation_split: SupportsIn = ",;:!?*%-+=<>)]}\\|/",
        goback_fraction: Optional[float] = 0.4,
        goback_count: Optional[int] = None,
) -> Union[str, List[str]]:
    text = str(obj)
    if len(text) <= line_length:
        return [text, ] if as_list else text
    if goback_fraction is None and goback_count is None:
        raise ValueError(
            "at least one of [max_part_without_word_boundaries, max_length_without_word_boundaries] must be not None"
        )
    goback_fraction = \
        goback_fraction or min(goback_count / line_length + 0.01, 1.0)
    goback_count = \
        goback_count or floor(goback_fraction * line_length)
    if (not (0 <= goback_fraction <= 100)) or (not (0<=goback_count<=line_length)):
        raise ValueError(
            f"goback_fraction and goback_count must be '0 <= goback_fraction <= 100'; "
            f"'0<=goback_count<=line_length' respectively\n  got ({goback_fraction}; {goback_count})"
        )
    parts = []
    __old_pos = 0
    __pos = 0
    while __pos < len(text):
        if len(text)-__pos <= line_length:
            parts.append(text[__pos:])
            return parts if as_list else "\n".join(parts)
        __pos += line_length
        __left_index = __pos - min(goback_count, floor(goback_fraction * line_length))
        for __temp_index in range(__pos, __left_index-1, -1):
            if text[__temp_index].isspace():
                parts.append(text[__old_pos:__temp_index])
                __old_pos = __temp_index + 1
                __pos = __temp_index + 1
                break
            if text[__temp_index] in allowed_punctuation_split:
                parts.append(text[__old_pos:__temp_index+1])
                __old_pos = __temp_index + 1
                __pos = __temp_index + 1
                break
            # todo: is_emoji?
            if __temp_index == __left_index:
                parts.append(text[__old_pos:__pos])
                __old_pos = __pos
                __pos += 1
                break


def align_left(
        obj: Union[str, Any], max_line_length: int = 120, overflow_mode: overflow_options = "ww", as_list: bool = False
) -> Union[str, List[str]]:
    __text = str(obj)
    parts = []
    if len(__text) > max_line_length:
        if overflow_mode in ("trunc_right", "tr"):
            parts.append(__text[0:max_line_length])
        elif overflow_mode:
            pass