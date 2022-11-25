def maxProfit(lengths, prices, rodLength):
    if len(lengths) == 0:
        return 0

    choice1 = 0
    if(lengths[0] <= rodLength):
        choice1 = maxProfit(lengths, prices, rodLength -
                            lengths[0]) + prices[0]

    choice2 = maxProfit(lengths[1:], prices[1:], rodLength)
    return max(choice1, choice2)


# dp[index][rodLength]
def maxProfitTopDown(lengths, prices, rodLength, index, dp):
    if index == len(lengths):
        return 0

    if dp[index][rodLength] != -1:
        return dp[index][rodLength]

    choice1 = 0
    if(lengths[index] <= rodLength):
        choice1 = maxProfitTopDown(lengths, prices, rodLength -
                                   lengths[index], index, dp) + prices[index]  # dp[index][rodLength - lengths[index]] + prices[index]

    # dp[index + 1][rodLength]
    choice2 = maxProfitTopDown(lengths, prices, rodLength, index + 1, dp)
    dp[index][rodLength] = max(choice1, choice2)

    return dp[index][rodLength]


# {index, rodLength} => state of DP
# dp[index][rodLength] = max(dp[index][rodLength - lengths[index]] + prices[index], dp[index + 1][rodLength])
# What do you need to know before filling the cell (index, rodLength) of the dp table?
#   -> You need to know dp[index][rodLength - length[index]] and dp[index + 1][rodLength]
#   -> Say length[index] is 2, What two cell do you need to know to calculate x?
"""
[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,y,0,x,0],
    [0,0,0,y,0],
    [0,0,0,0,0],
]
1. Just Above and just to left => Before i,j you should know i-1, j-1, for i in range(n), for j in range(m)
2. Just below and just to right => Before i,j you should know i+1,j+1, => i: range(n-1,-1, -1), j: range(m-1,-1,-1)
Correct => 3. Just below and two steps to left => Before i,j you should know i+1,j-l => i: range(n-1,-1,-1), j: range(m)
4. Just above and two steps to right => Before i,j you should know i-1,j+l => i: range(n), j: range(m-1,-1,-1)
"""

lengths = [1, 2, 3, 4, 5]
prices = [2, 6, 7, 10, 13]
rodLength = 5

print(maxProfit(lengths, prices, rodLength))

dp = [[-1]*6 for _ in range(5)]
print(maxProfitTopDown(lengths, prices, rodLength, 0, dp))
