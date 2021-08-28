
def sum_digits(num: int) -> int:
    res = 0
    while num > 0:
        res += num % 10
        num = num // 10

    return res


def sum_digits_recursive(num: int):
    if num == 0:
        return 0
    return num % 10 + sum_digits_recursive(num // 10)


if __name__ == '__main__':
    numbers = [1, 11, 111, 1111, 0, 9]
    print("Results for sum_digits()")
    for num in numbers:
        print(f"For {num} the sum of digits is: {sum_digits(num)}")

    print("")
    print("Results for sum_digits_recursive()")
    for num in numbers:
        print(f"For {num} the sum of digits is: {sum_digits_recursive(num)}")

