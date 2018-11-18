"""
Partition an integers array into odd number first and even number second.

Have you met this question in a real interview?
Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        odd = 0
        even = len(nums) - 1

        while odd <= even:
            if nums[odd] % 2 == 0 and nums[even] % 2 == 1:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 1
                even -= 1
            elif nums[even] % 2 == 0:
                even -= 1
            elif nums[odd] % 2 == 1:
                odd += 1
            else:
                odd += 1
                even -= 1

        return nums