"""
Test if a string is palindrome or not
"""


def is_palindrome(input_str: str ) -> bool:
    if len(input_str) == 1:
        return True

    palindrome_test = True
    length = len(input_str) - 1
    for i in range(0, len(input_str)//2):
        palindrome_test = palindrome_test and (input_str[i] == input_str[length-i])
        if not palindrome_test:
            break
    return palindrome_test


def is_palindrome_recursive(my_str: str, is_first: bool = True):
    if is_first:
        my_str = list(my_str)
        if len(my_str) == 1:
            return True

    end = len(my_str) - 1
    if (end == 1) or (len(my_str) == 1):
        return True

    return (my_str[0] == my_str[end]) and (is_palindrome_recursive(my_str[1: end], is_first=False))


def test_palindrome_result(res: bool, expected: bool, string_to_test: str):
    test = "***FAIL***"
    if res == test_is_palindrome[i]:
        test = "PASS"
    print(f"\tTest: {test}. Expected {expected}. Result is {res} for the string: '{string_to_test}'")


if __name__ == '__main__':
    string_to_test = ['123321', '1234321', '1234', '123', '1221', '1', '11']
    test_is_palindrome = [True, True, False, False, True, True, True]

    print("Testing is_palindrome():")
    for i, num in enumerate(string_to_test):
        res = is_palindrome(num)
        test_palindrome_result(res, test_is_palindrome[i], string_to_test[i])

    print("")
    print("Testing is_palindrome_recursive():")
    for i, num in enumerate(string_to_test):
        res = is_palindrome_recursive(num)
        test_palindrome_result(res, test_is_palindrome[i], string_to_test[i])





