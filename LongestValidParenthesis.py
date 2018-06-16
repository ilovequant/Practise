"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        if len(s) == 1:
            return 0

        stack = []
        n = len(s)
        maxlen = 0
        start = -1

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    start = i
                else:
                    temp = stack.pop()
                    if not stack:
                        maxlen = max(maxlen, i - start)
                    else:
                        maxlen = max(maxlen, i - stack[-1])

        return maxlen