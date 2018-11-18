"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(0, 0, res, "", n)
        return res

    def helper(self, l, r, res, s, n):
        if l == n and r == n:
            return res.append(s)

        if l < n:
            self.helper(l + 1, r, res, s + '(', n)

        if r < l:
            self.helper(l, r + 1, res, s + ')', n)

