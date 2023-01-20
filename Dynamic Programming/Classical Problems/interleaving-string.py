# https://leetcode.com/problems/interleaving-string/

# Brute Force Approach

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True

        if len(s3) == 0:
            return False

        answer = False

        if len(s1) > 0 and s1[0] == s3[0]:
            answer = answer or self.isInterleave(s1[1:], s2, s3[1:])

        if answer:
            return True

        if len(s2) > 0 and s2[0] == s3[0]:
            answer = answer or self.isInterleave(s1, s2[1:], s3[1:])

        return answer

# Top-down Memoization


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def helper(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if dp[i][j] != None:
                return dp[i][j]

            answer = False

            if len(s1) > i and s1[i] == s3[i + j]:
                answer = answer or helper(i+1, j)

            if answer:
                dp[i][j] = True
                return True

            if len(s2) > j and s2[j] == s3[i + j]:
                answer = answer or helper(i, j + 1)

            dp[i][j] = answer
            return answer

        return helper(0, 0)
