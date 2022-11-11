def addList(lst):
    if len(lst) == 0:
        return 0
    else:
        return addList(lst[1:]) + lst[0]

# Recursion = Base Case, Self-work, Recursive Assumption


print(addList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
