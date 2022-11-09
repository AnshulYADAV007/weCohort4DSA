
def merge(nums1, nums2):
    i1, i2, n1, n2 = 0, 0, len(nums1), len(nums2)
    answer = []
    while i1 < n1 and i2 < n2:
        if nums1[i1] < nums2[i2]:
            answer.append(nums1[i1])
            i1 += 1
        else:
            answer.append(nums2[i2])
            i2 += 1
    while i1 < n1:
        answer.append(nums1[i1])
        i1 += 1

    while i2 < n2:
        answer.append(nums2[i2])
        i2 += 1

    return answer


def mergeSort(nums):
    print(nums)  # [2,1,5,3] -> [2, 1] -> [2] -> [1]
    # -> [5,3] -> [5] -> [3]
    n = len(nums)
    if n <= 1:
        return nums  # Base case
    left = mergeSort(nums[:n//2])  # Recursion
    right = mergeSort(nums[n//2:])
    answer = merge(left, right)  # Self-work
    print(answer)  # [2] -> [1] -> [1,2] -> [5] -> [3]
    # -> [3,5] -> [1,2,3,5]
    return answer


mergeSort([2, 1, 5, 3])
