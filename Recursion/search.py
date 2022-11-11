# find the index of a target in a lst
def getIndex1(lst, target):
    if len(lst) == 0:
        return -1
    elif lst[-1] == target:
        return len(lst) - 1
    else:
        return getIndex1(lst[:-1], target)


def getIndex2(lst, target):
    if len(lst) == 0:
        return -1
    elif lst[0] == target:
        return 0
    else:
        index = getIndex2(lst[1:], target)
        return 1 + index if index >= 0 else -1


print(getIndex1([1, 7, 2, 3, 4, 5, 6, 7], 7))
print(getIndex2([1, 7, 2, 3, 4, 5, 6, 7], 7))
