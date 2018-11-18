class Solution:
    """
    @param str: a string
    @return: return a string
    """

    def reverseWords(self, str):
        # write your code here

        str = self.reverse(str)
        p1, p2 = 0, 0

        while (p2 <= len(str)):
            if (p2 < len(str) and str[p2] == " "):
                str = str[:p1] + self.reverse(str[p1:p2]) + str[p2:]
                p1 = p2 + 1

            if (p2 == len(str)):
                str = str[:p1] + self.reverse(str[p1:p2]) + str[p2:]

            p2 += 1

        return str

    def reverse(self, str):
        rev = ""
        for i in range(len(str)):
            rev += str[len(str) - i - 1]

        return rev