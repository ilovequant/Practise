"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example
Given pattern = "abba", str = "dog cat cat dog", return true.
Given pattern = "abba", str = "dog cat cat fish", return false.
Given pattern = "aaaa", str = "dog cat cat dog", return false.
Given pattern = "abba", str = "dog dog dog dog", return false.


test case:
pattern = "abba", str = "dog cat cat dog"
pattern = "abba", str = "dog dog dog dog"
"""


class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, str):
        # write your code here
        matching = str.split(' ')
        if len(pattern) != len(matching):
            return False
        count = 0
        map = {}
        for c in pattern:
            if c in map.keys():
                if map[c] != matching[count]:
                    return False
            else:
                if matching[count] not in map.values():
                    map[c] = matching[count]
                else:
                    return False

            count += 1

        return True