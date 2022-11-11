# return the sum of first n natural numbers

def sumInt(n):
    if n <= 0:
        return 0
    else:
        return sumInt(n - 1) + n


print(sumInt(100))
