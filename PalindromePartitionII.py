"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        n = len(s)
        dp = [float('Inf')] * n
        ispalin = self.isPalindrome(s)

        for i in range(n):
            if ispalin[0][i]:
                dp[i] = 0

        for i in range(n):
            for j in range(i):
                if ispalin[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n - 1]

    def isPalindrome(self, s):
        n = len(s)
        table = [[False] * n for x in range(n)]

        for i in range(n):
            table[i][i] = True

        if n > 1:
            for i in range(n - 1):
                if s[i] == s[i + 1]:
                    table[i][i + 1] = True

        if n > 2:
            for l in range(3, n + 1):
                for i in range(n - l + 1):
                    j = i + l - 1
                    if s[i] == s[j] and table[i + 1][j - 1]:
                        table[i][j] = True

        return table