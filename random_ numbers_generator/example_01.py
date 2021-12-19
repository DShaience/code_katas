import numpy as np


def random_numbers_without_seed():
    print("Generating random numbers without seed")
    for i in range(0, 3):
        print(np.random.randint(0, 10, 5))
    print("")
    # Each set is different. Implicitly using clock ts as seed
    # [5 8 7 3 9]
    # [3 6 9 3 9]
    # [0 7 4 6 7]


def random_number_with_seed():
    print("Generating random numbers with seed")
    for i in range(0, 3):
        np.random.seed(90210)
        print(np.random.randint(0, 10, 5))
    print("")
    # Repetitive numbers set
    # [5 6 5 8 5]
    # [5 6 5 8 5]
    # [5 6 5 8 5]


if __name__ == '__main__':
    # Example 1: Random numbers without seed:
    random_numbers_without_seed()

    # Example 2: Random numbers with seed:
    random_number_with_seed()


