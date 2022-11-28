// https://leetcode.com/problems/climbing-stairs/description/
class Solution {
public:
    int climbStairs(int n) {
        int last = 1, secondLast = 1;
        for(int i = 2; i <= n; i++) {
            int temp = last;
            last = last + secondLast;
            secondLast = temp;
        }
        return last;
    }
    // int climbStairs(int n) {
    //     // climbStairs(n) = climbStairs(n - 2) + climbStairs(n - 1)
    //     // Before calculating n, I should know n-2 and n-1
    //     vector<int> dp(n+1);
    //     dp[0] = 1;
    //     dp[1] = 1;
    //     for(int i = 2; i <= n ; i++) dp[i] = dp[i-1] + dp[i-2];
    //     return dp[n];
    // }
};