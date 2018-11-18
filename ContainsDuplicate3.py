class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        l = len(nums)
        d = {}
        if k == 0:
            return False

        for i in range(l):
            if t:
                bucketNum, offset = nums[i] // t, 1
            if not t:
                bucketNum, offset = nums[i], 0

            for j in range(bucketNum - offset, bucketNum + offset + 1):
                if j in d and abs(nums[i] - d[j]) <= t:
                    return True

            d[bucketNum] = nums[i]

            if len(d) > k:
                if t:
                    del d[nums[i - k] // t]
                else:
                    del d[nums[i - k]]

        return False
