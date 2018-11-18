class Solution:
    """
    @param str: A string
    @return: An integer
    """

    def atoi(self, str):
        # write your code here
        if not str:
            return 0

        # remove white space
        if "." in str:
            a, b, c = str.partition('.')
            str = a
        str = str.replace(" ", "")

        sign = 1
        # remove wrong operator +- or -+
        if "+-" in str:
            return 0

        # extract - or +
        if str[0] == '-':
            sign = -1
            str = str[1:]

        if str[0] == '+':
            str = str[1:]

        # if after extraction only 0
        if str == "0":
            return 0

        # delete no digitals
        for i in range(1, len(str)):
            if str[:i].isdigit() and not str[:i + 1].isdigit():
                str = str[:i]

        p = float('inf')

        # delete leading zeroes
        for i in range(len(str)):
            if str[i] != '0':
                p = min(p, i)

        str = str[p:]

        # if no digitals

        if str in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and str not in "1234567890":
            return 0

        str = sign * eval(str)

        if str > 2147483647:
            return 2147483647

        if str < -2147483648:
            return -2147483648
        return str