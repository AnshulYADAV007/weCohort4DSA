# Given the weights and profits of ‘N’ items,
# we are asked to put these items in a knapsack
# that has a capacity ‘C’. The goal is to get the
# maximum profit from the items in the knapsack.
# The only difference between the 0/1 Knapsack problem and
# this problem is that we are allowed to use an unlimited quantity of an item.

def unBoundedKnapsack(weights, profits, capacity):
    if len(weights) == 0:
        return 0

    choice1 = 0
    if(weights[0] <= capacity):
        choice1 = unBoundedKnapsack(weights, profits, capacity - weights[0]) \
            + profits[0]

    choice2 = unBoundedKnapsack(weights[1:], profits[1:], capacity)
    return max(choice1, choice2)


weights = [1, 2, 3]
profits = [15, 20, 50]
knapsack_capacity = 5
print(unBoundedKnapsack(weights, profits, knapsack_capacity))
# 1 * 5 => 15 * 5 = 75
# 1 * 1 + 2 * 2 => 15 + 20 * 2 = 55

# Say 63 -> not a multiple of 5
# Say 65 -> I can get it using 15, 15, 15, 20 => 1, 1, 1, 2

# Say 35 -> not an answer 20 + 15, problem is 1 + 2 = 3 and capacity is 5.
# So, there is extra capacity left. 1 + 1 + 1 + 2 = 5 or 1 + 2 + 2 = 5.
# 15 + 15 + 15 + 20 -> 65 or 15 + 20 + 20 -> 55
