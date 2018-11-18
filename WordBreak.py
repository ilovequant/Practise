***recursion:


class Solution:
    def wordBreak(self, s, dict):
        # write your code here
        if len(s) == 0 and len(dict) == 0:
            return True
        if not s or not dict:
            return False
        self.dict = dict
        self.seen = {}
        if self.canbreak(s):
            return True
        else:
            return False

    def canbreak(self, s):
        if s in self.seen:
            return self.seen[s]

        else:
            if s == "":
                return True
            for word in self.dict:
                if len(word) <= len(s) and s[:len(word)] == word:
                    if self.canbreak(s[len(word):]):
                        self.seen[s] = True
                        return True
        self.seen[s] = False
        return False

***dp solution memorize

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 and len(wordDict) == 0:
            return True
        if not s or not wordDict:
            return False
        dp = [False for i in range(len(s) + 1)]
        print(len(dp))
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            for word in wordDict:
                start = i
                end = i + len(word)

                if end > len(s):
                    continue

                else:
                    if s[start:end] == word:
                        dp[end] = True

        return dp[len(s)]