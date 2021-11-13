# https://www.hackerrank.com/challenges/merge-the-tools/problem

if __name__ == '__main__':
    s = 'AABCAAADA'
    k = 3

    assert len(s) % k == 0, "The length of s must me dividable by k"

    substrings = [set(s[i*k:k*(i+1)]) for i in range(0, k)]
    for substr in substrings:
        print("".join(list(substr)))

    