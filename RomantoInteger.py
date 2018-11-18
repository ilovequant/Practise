class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """

    def romanToInt(self, s):
        # write your code here
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if (i < len(s) - 1 and s[i] == 'I' and s[i + 1] != 'V' and s[i + 1] != 'X') or (
                    i == len(s) - 1 and s[i] == 'I'):
                res += dict['I']

            if i < len(s) - 1 and s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                res += -dict['I']

            if s[i] == 'V':
                res += dict['V']

            if (i < len(s) - 1 and s[i] == 'X' and s[i + 1] != 'L' and s[i + 1] != 'C') or (
                    i == len(s) - 1 and s[i] == 'X'):
                res += dict['X']

            if i < len(s) - 1 and s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                res += -dict['X']

            if s[i] == 'L':
                res += dict['L']

            if (i < len(s) - 1 and s[i] == 'C' and s[i + 1] != 'D' and s[i + 1] != 'M') or (
                    i == len(s) - 1 and s[i] == 'C'):
                res += dict['C']

            if i < len(s) - 1 and [i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                res += -dict['C']

            if s[i] == 'D':
                res += dict['D']

            if s[i] == 'M':
                res += dict['M']

        return res