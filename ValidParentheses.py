"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s is None:
            return False

        stack = []
        dict = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i in dict.values():
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack.pop() != dict[i]:
                        return False

        return len(stack) == 0