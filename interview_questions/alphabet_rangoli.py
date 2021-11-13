# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# size 5
#
"""
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#  (N-1) * 4 + 1 = 4N - 3
#

# size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""


class RangoLine:
    def __init__(self, N: int, ordered_letters_to_insert: list):
        # letters should be in a descending order
        self.N = N
        self.separator = '-'
        self.letters = ordered_letters_to_insert
        self.letters_to_embed = self.letters + self.letters[::-1][1:]

    def get_line(self) -> str:
        line = self.separator.join(self.letters_to_embed)
        line_target_len = 4*self.N - 3
        if len(line) < line_target_len:
            to_add = line_target_len - len(line)
            line = self.separator*(to_add//2) + line + self.separator*(to_add//2)
        return line



if __name__ == '__main__':
    N = 5

    lines = []
    alphabet_superset = [chr(i) for i in range(ord('a'), ord('a')+N)]
    reversed_alpha = alphabet_superset[::-1]
    num_letters_to_include = 0
    for line_num in range(1, N*2):
        lines.append(RangoLine(N, reversed_alpha[0:num_letters_to_include+1]).get_line())
        if line_num < N:
            num_letters_to_include += 1
        else:
            num_letters_to_include -= 1


    print("\n".join(lines))

















