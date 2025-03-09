from typing import Dict, Callable, Optional, Union, Any

from source.classes.progress.ProgressProcessor import ProgressProcessor
from globals_and_types import real_number


Callable_of_sections_min_max_cur_perc__to_str = Callable[[int, real_number, real_number, real_number, real_number], str]
dynamic_style_element = Union[Dict[bool, str], Callable_of_sections_min_max_cur_perc__to_str]


class GeneralProgressBarStyle:
    def __init__(
            self,
            filled_section: Optional[Any] = None,
            empty_section: Optional[Any] = None,

            bar_opener: Optional[Any] = None,
            separator: Optional[Any] = None,
            bar_closer: Optional[Any] = None,
            name: Optional[str] = None
    ):
        self.filled_section = filled_section
        self.empty_section = empty_section
        self.bar_opener = bar_opener
        self.separator = separator
        self.bar_closer = bar_closer
        self.name = name

    '''def clone(
            self,
            filled_section: Optional[dynamic_style_element] = None,
            empty_section: Optional[dynamic_style_element] = None,
            bar_opener: Optional[dynamic_style_element] = None,
            separator: Optional[dynamic_style_element] = None,
            bar_closer: Optional[dynamic_style_element] = None,
            name: Optional[str] = None
    ):
        new_style = GeneralProgressBarStyle()
        new_style.filled_section = filled_section or self.filled_section
        new_style.empty_section = empty_section or self.empty_section
        new_style.bar_opener = bar_opener or self.bar_opener
        new_style.separator = separator or self.separator
        new_style.bar_closer = bar_closer or self.bar_closer
        new_style.name = name
        return new_style'''
    def process_element(self, elem) -> str:
        raise NotImplementedError
    
    def __bool__(self):
        return self.filled_section is not None and self.empty_section is not None


class StaticProgressBarStyle(GeneralProgressBarStyle):
    def __init__(
            self,
            filled_section: Optional[str] = None,
            empty_section: Optional[str] = None,
            bar_opener: Optional[str] = None,
            separator: Optional[str] = None,
            bar_closer: Optional[str] = None,
            name: Optional[str] = None
    ):
        super().__init__(filled_section, empty_section, bar_opener, separator, bar_closer, name)
    
    def process_element(self, elem: Optional[str]) -> str:
        return elem or ""


class DynamicProgressBarStyle(GeneralProgressBarStyle):
    def __init__(
            self,
            filled_section: Optional[dynamic_style_element] = None,
            empty_section: Optional[dynamic_style_element] = None,
            bar_opener: Optional[dynamic_style_element] = None,
            separator: Optional[dynamic_style_element] = None,
            bar_closer: Optional[dynamic_style_element] = None,
            name: Optional[str] = None
    ):
        super().__init__(filled_section, empty_section, bar_opener, separator, bar_closer, name)

    def process_element(self, elem: Optional[dynamic_style_element], progress_data: ProgressProcessor) -> str:
        if elem is None:
            return ""
        if isinstance(elem, dict):
            # todo: как записать выражение?
            return elem[True]
        if isinstance(elem, Callable):
            pass





'''def combine_styles(
        style: Optional[GeneralProgressBarStyle] = None,

        new_filled_section: Optional[dynamic_style_element] = None,
        new_empty_section: Optional[dynamic_style_element] = None,
        new_bar_opener: Optional[dynamic_style_element] = None,
        new_separator: Optional[dynamic_style_element] = None,
        new_bar_closer: Optional[dynamic_style_element] = None
) -> GeneralProgressBarStyle:
    style = style or GeneralProgressBarStyle()
    style = style.clone(
        new_filled_section,
        new_empty_section,
        new_bar_opener,
        new_separator,
        new_bar_closer,
    )
    if not bool(style):
        raise ValueError("mandatory properties filled_section and empty_section weren't set in any way")
    return style'''
