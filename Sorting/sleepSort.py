from threading import Thread
from time import sleep


def routine(n):
    sleep(n)
    print(n)


def sleepSort(nums):
    for num in nums:
        thread = Thread(target=routine, args=(num,))
        thread.start()


sleepSort([3, 2, 5, 7, 4])
