
def partition(nums, left, right):
    pivot = nums[right]
    i = left - 1

    for j in range(left, right):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]

    nums[i+1], nums[right] = nums[right], nums[i + 1]
    return i + 1


def quickSort(nums, left, right):
    if left >= right:
        return
    pivotIndex = partition(nums, left, right)
    quickSort(nums, left, pivotIndex - 1)
    quickSort(nums, pivotIndex + 1, right)


nums = [5, 4, 3, 7, 6, 2, 1]
quickSort(nums, 0, len(nums)-1)
print("The sorted order is ", nums)
