"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n_chars = len(s)
    if n_chars <= 1:
        return

    n_midway = n_chars // 2
    for i in range(n_midway):
        c = s[i]
        s[i] = s[n_chars-i-1]
        s[n_chars - i - 1] = c


if __name__ == '__main__':
    pass

    s = list('avocadoo')
    reverseString(None, s)
    print(s)
