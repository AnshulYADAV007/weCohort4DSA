# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[n]

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0: return 0
    #     # To rob or not to rob that is the choice
    #     # rob(n) <- rob(n-1), rob(n-2)
    #     n = len(nums)
    #     rob = nums[n-1] + self.rob(nums[:n-2])
    #     notToRob = self.rob(nums[:n-1])
    #     return max(rob, notToRob)
