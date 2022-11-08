from maxHeap import MaxHeap


def findKSmallest(lst, k):
    heap = MaxHeap()
    for element in lst:  # O(n * log(k))
        if heap.isEmpty() or heap.getMax() > element:
            heap.insert(element)  # O(log(k))
        if heap.size() > k:
            heap.removeMax()  # O(log(k))
    return heap.heap


lst = [10, 9, 8, 12, 15, 8, 19, 21, 23]
k = 3

print("The 3 smallest elements of", lst, "are", findKSmallest(lst, k))
