# https://www.hackerrank.com/challenges/find-a-string/problem


class Substring:
    def __init__(self, start_idx: int, end_idx: int):
        self.start_idx = start_idx
        self.end_idx = end_idx

    def __len__(self):
        return self.end_idx - self.start_idx

    def show(self):
        print(f"({self.start_idx}, {self.end_idx})")


if __name__ == '__main__':

    my_str = 'ABCDCDC'
    substr = 'CDC'

    substrs = []
    str_idx = 0
    while str_idx < len(my_str) - 1:
        substr_idx = 0
        sub_str_pos = Substring(str_idx, str_idx)
        while (substr_idx < len(substr) - 1) & (my_str[str_idx + substr_idx] == substr[substr_idx]):
            substr_idx += 1
            sub_str_pos.end_idx += 1

        if len(sub_str_pos) > 0:
            substrs.append(sub_str_pos)

        str_idx += 1

    for i in range(0, len(substrs)):
        substrs[i].show()


