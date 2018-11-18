class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    # TLE
    def anagrams(self, strs):
        # write your code here
        res = []
        visited = set()
        for i in range(len(strs)):
            if i not in visited:
                res.append(strs[i])
            count = 0
            for j in range(i + 1, len(strs)):
                if self.isanagrams(strs[i], strs[j]) and j not in visited:
                    res.append(strs[j])
                    count += 1
                    visited.add(j)
            if count == 0 and strs[i] not in res[:-1] and i not in visited:
                res.remove(strs[i])

        return res

    def isanagrams(self, s, t):
        if len(s) != len(t):
            return False

        map = {}
        for c in s:
            if c not in map.keys():
                map[c] = 1
            else:
                map[c] += 1

        for c in t:
            if c not in map.keys():
                return False
            else:
                map[c] -= 1

        for i in map.values():
            if i != 0:
                return False

        return True


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        product = [1 for i in range(len(strs))]
        res = []
        index = {}

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                product[i] = product[i] * prime[ord(strs[i][j]) - ord('a')]
            if product[i] not in index.keys():
                index[product[i]] = [strs[i]]
            else:
                index[product[i]].append(strs[i])

        for key, value in index.items():
            if len(value) > 1:
                res += value

        return res
