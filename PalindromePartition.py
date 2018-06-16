"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]

        res = []
        self.helper(s, res, [], 0, len(s))
        return res

    def helper(self, s, res, temp, start, end):
        if start == end:
            res.append(temp[::])
            return

        for index in range(start, end):
            sub = s[start:index + 1]
            temp.append(sub)
            if sub == sub[::-1]:
                self.helper(s, res, temp, index + 1, end)
            temp.pop()
