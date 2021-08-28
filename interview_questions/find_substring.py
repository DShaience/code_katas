"""
Find the longer sequence of characters in string-A that are anywhere inside string-B
Source: Microsoft interview question
"""
import numpy as np


class Subsequence:
    def __init__(self):
        self.start_idx = None
        self.end_idx = None
        self.ended_sequence = None

    def is_empty_sequence(self):
        return (self.start_idx is None) and (self.end_idx is None)

    def sequence_length(self):
        if self.is_empty_sequence():
            return 0
        else:
            return self.end_idx - self.start_idx

    def is_initialized(self):
        return self.start_idx is not None

    def update_sequence(self, idx: int):
        if self.is_empty_sequence():
            self.start_idx = idx
            self.end_idx = idx + 1
        else:
            self.end_idx = idx + 1

    def end_sequence(self, idx: int):
        self.end_idx = idx + 1
        self.ended_sequence = True

    def is_ended_sequence(self):
        return self.ended_sequence is True


def find_longest_subsequence(str_a: str, str_b: str) -> Subsequence:
    curr_subsequence = Subsequence()
    sequence_list = []
    lengths_list = []
    str_b_set = set(str_b)
    for i, lt in enumerate(str_a):
        if lt in str_b_set:
            curr_subsequence.update_sequence(i)
        else:
            curr_subsequence.end_sequence(i)

        if (curr_subsequence.is_ended_sequence()) or (i == len(str_a) - 1):
            lengths_list.append(curr_subsequence.sequence_length())
            sequence_list.append(curr_subsequence)
            curr_subsequence = Subsequence()

    if all([length is None for length in lengths_list]):
        return Subsequence()

    max_len_idx = np.argmax(lengths_list)
    longest_subsequence = sequence_list[max_len_idx]
    return longest_subsequence


if __name__ == '__main__':

    str_a = 'abccczabczabczabczabcd'
    str_b = 'cadb'

    sub_sequence = find_longest_subsequence(str_a, str_b)
    if not sub_sequence.is_empty_sequence():
        print(f"The longest subsequence is [{sub_sequence.start_idx}, {sub_sequence.end_idx}]: {list(str_a)[sub_sequence.start_idx:sub_sequence.end_idx]}")










