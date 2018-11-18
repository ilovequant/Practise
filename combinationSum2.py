class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)

        combinations = []
        combination = []
        self.dfs(combinations, combination, 0, candidates, target)

        return combinations

    def dfs(self, combinations, combination, startIndex, candidates, target):
        if (target == 0):
            combinations.append(list(combination))

        for i in range(startIndex, len(candidates)):
            if target < candidates[i]:
                break

            elif i > startIndex and candidates[i] == candidates[i - 1]:
                continue

            combination.append(candidates[i])
            self.dfs(combinations, combination, i + 1, candidates, target - candidates[i])
            combination.pop()