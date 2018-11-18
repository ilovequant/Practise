class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def union(self, x, y):
            parent_x = self.find(x)
            parent_y = self.find(y)

            if (parent_x != parent_y):
                self.parent[parent_x] = parent_y

        def find(self, v):
            if (self.parent[v] == v):
                return v

            self.parent[v] = self.find(self.parent[v])

            return self.parent[v]

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if (not edges or len(edges) == 0):
            return res

        uf = Solution.UnionFind(len(edges) + 1)

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]

            if (uf.find(a) == uf.find(b)):
                res.append(a)
                res.append(b)
                break

            else:
                uf.union(a, b)

        return res