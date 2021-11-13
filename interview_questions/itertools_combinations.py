# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == '__main__':
    S = 'HACK'
    k = 2

    str_combs = [sorted(list(combinations(S, n_chars))) for n_chars in range(1, k+1)]
    str_combs_flattened = [item for sublist in str_combs for item in sublist]

    str_combs_sorted = ["".join(sorted(x)) for x in str_combs_flattened]
    for sc in str_combs_sorted:
        print(sc)

