class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """

    def findStrobogrammatic(self, n):
        # write your code here
        res = []
        if n < 0:
            return res

        if n == 0:
            return ['']

        if n == 1:
            return ['0', '1', '8']

        table = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}

        if n % 2 == 0:
            self.dfs(res, table, n, '')
            return res

        self.dfs(res, table, n - 1, '')
        res_new = []
        for s in res:
            temp = ['0', '1', '8']
            for i in temp:
                res_new.append(s[:n // 2] + i + s[n // 2:])

        return res_new

    def dfs(self, res, table, n, s):

        if len(s) == n // 2:
            res.append(self.replicate(s[:], n, table))
            return

        for item in table.keys():
            if s == '' and item == '0':
                continue
            s += item
            self.dfs(res, table, n, s)
            s = s[:-1]

    def replicate(self, s, n, table):
        end = n // 2 - 1
        while end >= 0:
            s += table[s[end]]
            end -= 1

        return s
