class K(str):
    def __lt__(x, y):
        return y + x < x + y


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        sorted_nums = sorted(map(str, nums), key=K)
        if sorted_nums[0] != "0":
            return "".join(sorted_nums)
        else:
            return "0"




"""
second approach:
"""


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        def cmp_to_key(cmp):
            class K:
                def __init__(self, object):
                    self.object = object

                def __lt__(self, other):
                    return cmp(self.object, other.object) < 0

            return K

        sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare))
        if sorted_nums[0] != "0":
            return "".join(sorted_nums)
        else:
            return "0"