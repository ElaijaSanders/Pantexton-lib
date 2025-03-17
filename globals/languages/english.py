# region VALUES
from typing import List

base_digits = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
x_teens = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
x_tys = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
names_of_powers_of_ten = (
    "hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
    "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion",
    "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion"
)

numeric_forms = (
    "zero",
    "one",
    "some",
    "many",
    "fractional"
)
# endregion


# region FUNCTIONS
def int_to_words(number: int, groups_separator: str = " ", include_zeros: bool = False) -> str:
    if number == 0:
        return "zero"
    was_negative: bool = bool(number < 0)
    __remainder = abs(number)
    if __remainder >= 10**64:
        raise NotImplementedError("function int_to_words() supports numbers up to +-10^64 not inclusive")
    groups: List[str] = []
    __groups_count = 0
    while __remainder > 0:
        __group = __remainder % 1000
        __remainder //= 1000
        if __group > 0:
            __hundreds: int = __group // 100
            __tens: int = (__group % 100) // 10
            __ones: int = __group % 10
            __hundreds_word: str = (
                f"{base_digits[__hundreds]} hundred"
                if __hundreds > 0 or (include_zeros and __groups_count == 0)
                else ""
            )
            __t_o_words: str = ""
            if __tens == 0:
                __t_o_words = (base_digits[__ones] if __ones > 0 else "")
            elif __tens == 1:
                __t_o_words = x_teens[__ones]
            else:  # 2 <= __tens <= 9
                if __tens and __ones:
                    __t_o_words = f"{x_tys[__tens-2]}-{base_digits[__ones]}"
                elif __tens:
                    __t_o_words = x_tys[__tens-2]
                else:  # if __ones
                    __t_o_words = base_digits[__ones]
            __power_10: str = names_of_powers_of_ten[__groups_count] if __groups_count > 0 else ""
            __group_res: str =  " ".join([__elem for __elem in (__hundreds_word, __t_o_words, __power_10) if __elem])
        elif __group == 0 and not include_zeros:
            __group_res: str = ""
        else:
            __group_res: str = f"zero {names_of_powers_of_ten[__groups_count]}" \
                if __groups_count > 0 \
                else "zero hundred zero"
        groups.append(__group_res)
        __groups_count += 1
    groups.reverse()
    result = groups_separator.join([__elem for __elem in groups if __elem])
    if was_negative:
        result = "minus " + result
    return result


def float_to_words(number: float):
    pass
# endregion
