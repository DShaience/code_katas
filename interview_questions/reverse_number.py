"""
Write a program to reverse a number
"""
import math


def reverse_number_with_loop(num: int):
    if num == 0:
        return 0
    num_digits = int(round(math.log10(num) + 0.5))
    print(num_digits)
    num_array = []
    for digit_idx in range(0, num_digits):
        mod = num % 10
        num = num // 10
        num_array.append(mod)
    i = 0
    while num_array[i] == 0:
        i += 1

    return "".join([str(num) for num in num_array[i:]])


def rev_num_recursive(num: int, is_first: bool = True):
    # remove least-significant sequence of 0, if exists
    if is_first:
        while (num > 0) and (num % 10 == 0):
            num = num // 10
        if num == 0:
            return "0"

    if num == 0:
        return ""

    return str(num % 10) + str(rev_num_recursive(num // 10, is_first=False))


def rev_num_string_method(num: int):
    if num == 0:
        return "0"

    num_str = list(str(num))
    num_str_reversed = num_str[::-1]
    i = 0
    while num_str_reversed[i] == "0":
        i += 1

    num_str_reversed_no_leading_zeroes = num_str_reversed[i:]
    return "".join(num_str_reversed_no_leading_zeroes)


if __name__ == '__main__':
    num = 12340100
    print(reverse_number_with_loop(num))
    print(rev_num_recursive(num))
    print(rev_num_string_method(num))



