class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        combination = []
        # candidates = sorted(list(set(candidates)))
        self.dfs(combinations, combination, 0, self.sortAndRemoveduplicate(candidates), target)
        return combinations

    def dfs(self, combinations, combination, startIndex, candidates, target):
        if target == 0:
            combinations.append(list(combination))
            return

        for i in range(startIndex, len(candidates)):
            if target < candidates[i]:
                return
            combination.append(candidates[i])
            self.dfs(combinations, combination, i, candidates, target - candidates[i])
            combination.pop()

    def sortAndRemoveduplicate(self, candidates):
        candidates = sorted(candidates)
        index = 0
        for i in range(len(candidates)):
            if candidates[i] != candidates[index]:
                index += 1
                candidates[index] = candidates[i]

        new_candidates = []

        for i in range(index + 1):
            new_candidates.append(candidates[i])

        return new_candidates