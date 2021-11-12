# https://www.hackerrank.com/challenges/find-a-string/problem


class Substring:
    def __init__(self, start_idx: int, end_idx: int):
        self.start_idx = start_idx
        self.end_idx = end_idx

    def __len__(self):
        return self.end_idx - self.start_idx

    def show(self):
        print(f"({self.start_idx}, {self.end_idx})")

    def get_range(self):
        return range(self.start_idx, self.end_idx)


if __name__ == '__main__':

    """
    Algorithm
    1. run over the entire string 1-n with str_idx until the end
    1.1. run over the substring 1-m with sb_str_idx until the end (check for of out-of-bounds with str_idx)
    1.2. if the entire substr matches, add indices of start and end 
    """

    org_str = 'ABCDCDC'
    sub_str = 'CDC'

    # org_str = 'DDDDDDD'
    # sub_str = 'D'

    n_org = len(org_str)
    n_sub = len(sub_str)

    org_idx = 0
    matches = []
    while org_idx < n_org:

        remaining_chars_org = n_org - org_idx
        if remaining_chars_org < n_sub:
            break

        if org_str[org_idx:(org_idx+n_sub)] == sub_str:
            matches.append(Substring(org_idx, org_idx+n_sub))

        org_idx += 1


    for i in range(0, len(matches)):
        matches[i].show()
        print(org_str[matches[i].start_idx: matches[i].end_idx])

    print(f"\nTotal number of matches: {len(matches)}")






