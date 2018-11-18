class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false

    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Have you met this question in a real interview?
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.



    """

    def validTree(self, n, edges):
        # write your code here

        if n == 1 and len(edges) == 0:
            return True

        if len(edges) != n - 1:
            return False

        map = {}
        for i in range(len(edges)):
            if edges[i][0] in map.keys():
                map.get(edges[i][0]).append(edges[i][1])

            if edges[i][0] not in map.keys():
                map[edges[i][0]] = []
                map[edges[i][0]].append(edges[i][1])

            if edges[i][1] in map.keys():
                map.get(edges[i][1]).append(edges[i][0])

            if edges[i][1] not in map.keys():
                map[edges[i][1]] = []
                map[edges[i][1]].append(edges[i][0])

        queue = []
        visited = set()
        queue.append(edges[0][0])
        visited.add(edges[0][0])
        count = 0

        while queue:
            temp = queue.pop()
            count += 1
            for neighbor in map[temp]:
                if neighbor in queue:
                    return False

                if neighbor not in visited:
                    queue.insert(0, neighbor)
                    visited.add(neighbor)

        return count == n