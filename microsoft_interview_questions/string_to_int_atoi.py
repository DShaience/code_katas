"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
    This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
    Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""



def myAtoi(self, s: str) -> int:
    i = 0

    sign = 1
    n_chars = len(s)
    digits = []
    if i == 0:
        while (i < n_chars-1) and s[i].isspace():
            i += 1

    if (i < n_chars-1) and s[i] in ['+', '-']:
        if s[i] == '-':
            sign = -1
        i += 1

    while (i < n_chars) and s[i].isdigit():
        digits.append(s[i])
        i += 1

    if len(digits) == 0:
        return 0
    else:
        as_num = int("".join(digits)) * sign
        if as_num < -(2**31):
            return -(2**31)
        elif as_num > (2**31) - 1:
            return (2**31) - 1
        else:
            return as_num




if __name__ == '__main__':
    # s = "   -42"
    s = "+1"
    print(myAtoi(None, s))





        # i += 1

    # print(s[i:])










