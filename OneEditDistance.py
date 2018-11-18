class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """

    def isOneEditDistance(self, s, t):
        # write your code here
        ls = len(s)
        lt = len(t)

        p1 = 0
        p2 = 0
        count = 0

        if s == t:
            return False

        if ls == lt:
            while (p1 < ls and p2 < lt):
                if s[p1] != t[p2]:
                    count += 1
                    if count > 1:
                        return False
                p1 += 1
                p2 += 1
            if p1 == ls and p2 == lt:
                return True

        p1 = 0
        p2 = 0
        count = 0

        if ls - lt == 1:
            while (p1 < ls and p2 < lt):
                if count == 0 and s[p1] != t[p2]:
                    p1 += 1
                    count += 1

                if count > 0 and s[p1] != t[p2]:
                    return False

                p1 += 1
                p2 += 1

            return True

        p1 = 0
        p2 = 0
        count = 0

        if lt - ls == 1:
            while (p1 < ls and p2 < lt):
                if count == 0 and s[p1] != t[p2]:
                    p2 += 1
                    count += 1

                if count > 0 and s[p1] != t[p2]:
                    return False

                p1 += 1
                p2 += 1

            return True

        else:
            return False