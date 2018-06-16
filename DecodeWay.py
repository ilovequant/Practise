"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        a = 0
        b = 0

        for i in range(1, n):
            if s[i] == '0' and (s[i - 1] > '2' or s[i - 1] == '0'): return 0
            a = dp[i] if s[i] != '0' else 0
            b = dp[i - 1] if '09' < s[i - 1:i + 1] < '27' else 0
            dp[i + 1] = a + b

        return dp[n]