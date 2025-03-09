from typing import Optional

from globals_and_types import real_number


class ProgressProcessor:
    def __init__(
            self,
            start: real_number = 0,
            stop: real_number = 100,
            current_value: Optional[real_number] = None,
    ):
        self.start = start
        self.stop = stop
        self.current_value = current_value or start

    def __len__(self) -> real_number:
        return abs(self.stop - self.start)

    def __str__(self):
        return f"start: {self.start} | current: {self.__current_value} | stop: {self.stop}  " \
               f"({self.percent}% / {self.__len__()})"

    @property
    def percent(self) -> float:
        if (length := self.__len__()) == 0:
            return 100.0
        return abs(self.__current_value - self.start) * 100 / length

    @property
    def current_value(self) -> real_number:
        return self.__current_value

    @current_value.setter
    def current_value(self, value: real_number):
        if not (min(self.start, self.stop) <= value <= max(self.start, self.stop)):
            raise ValueError(
                f"value is {value}, but must be in 'start <= value <= stop'\n  "
                f"(or 'stop <= value <= start' in case of stop <= start)"
            )
        self.__current_value = value


class TimedProgressProcessor(ProgressProcessor):
    


__all__ = ("ProgressProcessor",)
