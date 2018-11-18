class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        self.backtracking(res, "", digits, dict)
        return res

    def backtracking(self, res, ans, digits, dict):
        if len(ans) == len(digits):
            res.append(ans)
            return

        digit = digits[len(ans)]
        for i in range(len(dict[digit])):
            ans += dict[digit][i]
            self.backtracking(res, ans, digits, dict)
            ans = ans[:-1]