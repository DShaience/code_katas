"""
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Input: s = ["a"]
Output: ["a"]

Constraints:
    1 <= s.length <= 105
    s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
    There is at least one word in s.
    s does not contain leading or trailing spaces.
    All the words in s are guaranteed to be separated by a single space.


"""
from typing import List




class Solution:
    @staticmethod
    def reverseWords(s: List[str]) -> None:
        n = len(s)
        if n == 1:
            return

        def swap(a, b):
            return b, a

        def reverse(s):
            for i in range(0, n//2):
                s[i], s[n-i-1] = swap(s[i], s[n-i-1])

        reverse(s)
        i = 0
        while i < n:
            j = i
            while (j < n) and (s[j].isalnum()):
                j += 1

            if j == i:
                i += 1
                continue
            else:
                diff = (j - i) // 2
                for k in range(0, diff):
                    s[k+i], s[j-k-1] = swap(s[k+i], s[j-k-1])
                i = j
        return


if __name__ == '__main__':
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Solution.reverseWords(s)
    print(s)
