# Question : https://leetcode.com/problems/decode-ways/?envType=list&id=ovutwbx5

class Solution:
    def numDecodings(self, s: str) -> int:
        # Options:
        # dp[i -> index] = the number of ways to decode the string s[i:]
        # dp[i -> index] = the number of ways to decode the string s[: i]
        # let dp[i]  = the number of ways to decode the first i characters
        # dp[0] = 1,
        # dp[1] = 1 if s[0] != '0' else 0
        # dp[i] = dp[i-1] + dp[i-2] if s[i-2: i] is less than 26 else dp[i-1]
        # '123' -> ? dp[n]
        # '1'  -> 'a' -> 1
        # '12' -> 'ab', 'l' -> 2
        # '123' -> '12' + '3' -> {'ab', 'l'} + 'c'
        # '123' -> '1' + '23' -> {'a'} + 'w'

        # '129' -> dp[n]
        # '1' -> 'a'
        # '12' -> 'ab', 'l'
        # '129' -> '12' + '9' -> {'ab', 'l'} + 'i'
