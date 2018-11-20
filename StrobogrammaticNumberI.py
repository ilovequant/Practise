class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def findStrobogrammatic(self, n):
        # write your code here
        res = []
        if n <= 0:
            return res

        table = set([6, 9, 0, 1, 8])
        self.dfs(res, table, n, '')
        return res

    def dfs(self, res, table, n, s):
        if len(s) == n // 2:
            if n % 2 == 0 or s[-1] not in {'6', '9'}:
                res.append(s[:])
                return

        for item in table:
            s += str(item)
            self.dfs(res, table, n, s)
            s = s[:-1]