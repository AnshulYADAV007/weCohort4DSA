import heapq


def maxSum(nums):  # O(n(log(n)))
    answer = nums[0]
    current = 0
    minHeap = [0]
    heapq.heapify(minHeap)
    for i in range(len(nums)):  # O(n)
        print(current, answer, minHeap)
        current += nums[i]
        answer = max(answer, current - minHeap[0])
        heapq.heappush(minHeap, current)  # O(log(n))
        print(current, answer, minHeap)
    return answer


def kadane(nums):
    current = 0
    answer = nums[0]
    for num in nums:
        current = max(0, current)
        current += num
        answer = max(answer, current)
    return answer


nums = [-1, -2, 3, 4, -2, -2, -4,  4, 5, -8]
#            |  -------------->|   ----->  |
#       -1, -3, 0, 4,  2,  0, -4,  0, 5, -3
# MinHeap is a min heap of all the prefix sums.
print(kadane(nums))
