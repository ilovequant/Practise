class Solution:
    """
    backtracking etl
    """

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [[] for i in range(len(s) + 1)]
        self.helper(res, s, len(s), 0)
        for item in res:
            if item:
                break

        if item == []:
            return [""]
        return item

    def helper(self, res, s, n, layer):
        if n == 0:
            return

        if self.isValid(s) and s not in res[layer]:
            res[layer].append(s)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(' or s[i] == ')':
                temp = ""
                temp = s
                s = s[:i] + s[i + 1:]
                self.helper(res, s, n - 1, layer + 1)
                s = temp
            else:
                continue

    def isValid(self, t):
        l = []
        r = []

        for c in t:
            if c == '(':
                l.append(')')
            elif c == ')':
                if l and c == l.pop():
                    continue

        for i in range(len(t) - 1, -1, -1):
            if t[i] == ')':
                r.append('(')
            elif t[i] == '(':
                if r and t[i] == r.pop():
                    continue

        if not l and not r:
            return True

        else:
            return False
