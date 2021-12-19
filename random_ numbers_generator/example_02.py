import numpy as np


def random_number_with_seed(n_to_generate: int):
    for i in range(0, 3):
        print(np.random.randint(0, 10, n_to_generate))
    print("")


if __name__ == '__main__':
    np.random.seed(90210)

    # Change to the first will also change the second (!)

    print("Produce some random numbers")
    random_number_with_seed(3)

    print("Produce some MORE random numbers")
    random_number_with_seed(3)




