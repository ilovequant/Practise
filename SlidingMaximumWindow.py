from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        res = []

        if not nums or len(nums) == 0:
            return res
        dq = deque([])

        def push(dq, nums, i):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        for i in range(k - 1):
            push(dq, nums, i)

        for i in range(k - 1, len(nums)):
            push(dq, nums, i)
            res.append(nums[dq[0]])

            if dq[0] == i - k + 1:
                dq.popleft()

        return res