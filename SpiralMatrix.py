class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """

    def spiralOrder(self, matrix):
        # write your code here
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = n - 1
        t = 0
        b = m - 1
        res = []

        while (l < r and t < b):
            for i in range(l, r + 1):
                res.append(matrix[t][i])

            for j in range(t + 1, b):
                res.append(matrix[j][r])

            for k in range(r, l - 1, -1):
                res.append(matrix[b][k])

            for p in range(b - 1, t, -1):
                res.append(matrix[p][l])

            l += 1
            r -= 1
            t += 1
            b -= 1

        if l == r and t < b:
            for i in range(t, b + 1):
                res.append(matrix[i][l])

        if l < r and t == b:
            for j in range(l, r + 1):
                res.append(matrix[t][j])

        if l == r and t == b:
            res.append(matrix[t][l])

        return res