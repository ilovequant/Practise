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

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if (not edges or len(edges) == 0 or edges[0] is None):
            return None

        vertex = set()
        parent = {}
        candidate = []
        for edge in edges:
            a = edge[0]
            b = edge[1]
            vertex.add(a)
            vertex.add(b)

            if b not in parent.keys():
                parent[b] = a
                continue

            candidate.append([parent[b], b])
            candidate.append([a, b])

            edge[1] = 0

        uf = Solution.UnionFind(len(vertex) + 1)

        for edge in edges:
            if edge[1] == 0:
                continue

            a = edge[0]
            b = edge[1]

            if uf.find(a) == uf.find(b):
                if len(candidate) == 0:
                    return edge

                return candidate[0]

            uf.union(a, b)

        return candidate[1]
