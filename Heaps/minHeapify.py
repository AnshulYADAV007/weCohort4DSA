def getSmallest(maxHeap, index, left, right):
    answer = index
    if left < len(maxHeap) and maxHeap[answer] > maxHeap[left]:
        answer = left
    if right < len(maxHeap) and maxHeap[answer] > maxHeap[right]:
        answer = right
    return answer


def minHeapify(maxHeap, index):
    smallest = getSmallest(maxHeap, index, index * 2 + 1, index * 2 + 2)
    if smallest != index:
        maxHeap[index], maxHeap[smallest] = maxHeap[smallest], maxHeap[index]
        minHeapify(maxHeap, smallest)
    return maxHeap


def convertMax(maxHeap):
    for i in range(len(maxHeap) - 1, -1, -1):
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap


maxHeap = [10, 9, 8, 7, 5, 3, 2]
print("The converted version of", maxHeap, "is", convertMax(maxHeap.copy()))
