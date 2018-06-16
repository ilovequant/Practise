"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if not S and not T:
            return True

        return self.twopointer(T) == self.twopointer(S)

    def twopointer(self, s):

        if len(s) == 1:
            if s == "#":
                return ""
            else:
                return s

        fast = 0
        slow = 0
        n = len(s)
        s_new = ""

        while (fast < n):
            if s[fast].islower():
                s_new += s[fast]
                fast += 1

            elif s[fast] == '#':
                if len(s_new) > 0:
                    s_new = s_new[:-1]
                fast += 1

        return s_new