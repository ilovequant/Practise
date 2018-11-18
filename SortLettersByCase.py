"""
Given a string which contains only letters. Sort it by lower case first and upper case second.

It's NOT necessary to keep the original order of lower-case letters and upper case letters.

Example
For "abAcD", a reasonable answer is "acbAD"

Challenge
Do it in one-pass and in-place.
"""



class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        left = 0
        right = len(chars) - 1
        while left < right:
            if 97 <= ord(chars[left]) <= 122:
                left += 1
            if 65 <= ord(chars[right]) <= 90:
                right -= 1
            if ord(chars[left]) < 97 and ord(chars[right]) > 90:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1