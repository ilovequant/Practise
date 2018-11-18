"""
Description
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

You are not necessary to keep the original order of positive integers or negative integers.

Have you met this question in a real interview?
Example
Given [-1, -2, -3, 4, 5, 6], after re-range, it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

Challenge
Do it in-place and without extra memory.
"""


class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here

        n = len(A)
        A.sort()
        pos = 0
        neg = 0
        for i in A:
            if i > 0:
                pos += 1
            else:
                neg += 1

        left = 0
        right = n - 1

        if n % 2 == 0:

            while left + 1 < right - 1:
                A[left + 1], A[right - 1] = A[right - 1], A[left + 1]
                left += 2
                right -= 2

        if n % 2 == 1:
            if neg > pos:
                while left + 1 < right:
                    A[left + 1], A[right] = A[right], A[left + 1]
                    left += 2
                    right -= 2

            else:
                while left < right - 1:
                    A[left], A[right - 1] = A[right - 1], A[left]
                    left += 2
                    right -= 2

        return A
