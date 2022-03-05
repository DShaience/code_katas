"""
Find the longest sequence of characters in string-A that are anywhere inside string-B
Source: Microsoft interview question
"""


class SubSequence:
    def __init__(self, start_idx, end_idx):
        self.start_idx = start_idx
        self.end_idx = end_idx

    def __len__(self):
        return self.end_idx - self.start_idx


def find_longest_sequence(str_a, str_b):
    str_b_set = set(str_b)
    n_str_a = len(str_a)
    longest_subseq = SubSequence(0, 0)
    i = 0
    while i < n_str_a:  # oABCo  len = 5
        j = i
        while (j < n_str_a) and (str_a[j] in str_b_set):
            j += 1
        if j - i > len(longest_subseq):
            longest_subseq = SubSequence(i, j)

        if j > i:
            i = j
        else:
            i += 1

    return longest_subseq


def solution(str_a, str_b):
    seq = find_longest_sequence(str_a, str_b)
    print(f"The longer sequence's length is: {len(seq)}")
    print(f"The longer sequence is: {str_a[seq.start_idx:seq.end_idx]}")


if __name__ == '__main__':
    str_a = 'abccczabczabczabczabcd'
    str_b = 'cadb'

    solution(str_a, str_b)




