import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = [float('-inf')] * k
        heapq.heapify(minheap)

        for i in range(len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, nums[i])

        return minheap[0]

    #time complexity: o(n + (n-k)*logk) space: o(k)