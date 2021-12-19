import numpy as np
import numpy.random


def random_number_with_random_state(rs: numpy.random.RandomState, n_to_generate: int):
    for i in range(0, 3):
        print(rs.randint(0, 10, n_to_generate))
    print("")


if __name__ == '__main__':
    random_process_A = np.random.RandomState(90210)
    random_process_B = np.random.RandomState(42)

    print("Produce some random numbers")
    random_number_with_random_state(random_process_A, 4)

    print("Produce some MORE random numbers")
    random_number_with_random_state(random_process_B, 3)




