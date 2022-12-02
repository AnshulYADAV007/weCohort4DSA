from functools import lru_cache


def findLCSLength(s1, s2):
    @lru_cache(10000)
    def helper(i1, i2):  # dp[i1][i2][count] = 4
        if i1 == len(s1) or i2 == len(s2):
            return 0

        choice1 = 0
        if s1[i1] == s2[i2]:
            choice1 = 1 + helper(i1 + 1, i2 + 1)

        choice2 = helper(i1 + 1, i2)
        choice3 = helper(i1, i2 + 1)

        return max([choice1, choice2, choice3])
    return helper(0, 0)


def lcsLengthRecursive(s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count

    choice1 = 0
    if s1[i1] == s2[i2]:
        choice1 = lcsLengthRecursive(s1, s2, i1 + 1, i2 + 1, count + 1)

    choice2 = lcsLengthRecursive(s1, s2, i1 + 1, i2, count)
    choice3 = lcsLengthRecursive(s1, s2, i1, i2 + 1, count)

    return max([choice1, choice2, choice3])


print(findLCSLength("passport", "psspt"))
