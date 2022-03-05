"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

"""


class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        s_new = []
        i = 0
        n = len(s)
        while i < n:
            while (i < n) and (s[i] == ' '):
                i += 1

            j = i
            while (j < n) and (s[j].isalnum()):
                j += 1
            if i < j:
                s_new.append(s[i:j])
                i = j
            else:
                i += 1

        return " ".join(s_new[::-1])


if __name__ == '__main__':
    print(Solution.reverseWords("the sky is blue"))

