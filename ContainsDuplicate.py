class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for idx, value in enumerate(nums):
            if value not in dict:
                dict[value] = idx

            else:
                if idx - dict[value] <= k:
                    return True
                else:
                    dict[value] = idx

        return False