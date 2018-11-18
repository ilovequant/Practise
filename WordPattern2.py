"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.
"""


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, str):
        # write your code here
        if len(pattern) == 1:
            return True
        map = {}
        return self.helper(0, 0, pattern, str, map)

    def helper(self, p, q, pattern, str, map):
        if (p == len(pattern) and q == len(str)): return True
        if (p == len(pattern) or q == len(str)): return False
        c = pattern[p]
        for i in range(q, len(str)):
            t = str[q:i + 1]
            if c in map and map[c] == t:
                if self.helper(p + 1, i + 1, pattern, str, map):
                    return True
            elif c not in map:
                if t not in map.values():
                    map[c] = t
                    if self.helper(p + 1, i + 1, pattern, str, map):
                        return True
                    del map[c]

        return False