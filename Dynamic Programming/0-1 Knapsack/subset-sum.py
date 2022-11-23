from functools import lru_cache
import random
# Given a set of positive numbers, determine if there exists a
# subset whose sum is equal to a given number ‘S’.

callCount = 0
maxDepth = 0


def subsetSumBruteForce(nums, S, depth):  # O (2 ^ (n + 1) - 1)
    # print("   " * depth, nums, S)
    # global callCount
    # callCount += 1
    # global maxDepth
    # maxDepth = max(maxDepth, depth)
    if len(nums) == 0:
        return S == 0
    choice1 = False
    if nums[0] <= S:
        choice1 = subsetSumBruteForce(nums[1:], S - nums[0], depth + 1)
    choice2 = subsetSumBruteForce(nums[1:], S, depth + 1)
    return choice1 or choice2


nums = [random.randint(0, 10) for _ in range(10)]
S = random.randint(0, 35)
print(nums, S, subsetSumBruteForce(nums, S, depth=0))
# for i in range(1, 15):
#     callCount = 0
#     nums = [random.randint(0, 10) for _ in range(i)]
#     S = random.randint(0, 10 * i)
#     subsetSumBruteForce(nums, S, 0)
#     print(i, callCount)


@lru_cache(1000)
def subsetSumTopDown(index, S):
    global callCount
    callCount += 1
    if index == len(nums):
        return S == 0
    choice1 = False
    if(nums[index] <= S):
        choice1 = subsetSumTopDown(index + 1, S - nums[index])
    if(choice1):
        return True
    choice2 = subsetSumTopDown(index + 1, S)
    return choice1 or choice2


for i in range(1, 15):
    callCount = 0
    nums = [random.randint(0, 10) for _ in range(i)]
    S = random.randint(0, 10 * i)
    subsetSumTopDown(0, S)
    print(i, callCount)
