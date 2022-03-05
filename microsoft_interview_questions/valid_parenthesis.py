"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:

        expected_closers = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        expected_closers_queue = []
        for i in range(len(s)):
            if s[i] in expected_closers:
                expected_closers_queue.append(expected_closers[s[i]])
            else:
                if (len(expected_closers_queue) > 0) and (s[i] == expected_closers_queue[-1]):
                    expected_closers_queue.pop()
                else:
                    return False

        return len(expected_closers_queue) == 0


if __name__ == '__main__':
    s = "()[]{}"
    # s = "([)]"
    # s = "(([)])"
    print(Solution.isValid(s))
